# 10. Regular Expression Matching
# Hard

# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.

# The matching should cover the entire input string (not partial).

# Note:

#     s could be empty and contains only lowercase letters a-z.
#     p could be empty and contains only lowercase letters a-z, and characters like . or *.

# Example 1:
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".

# Example 2:
# Input:
# s = "aa"
# p = "a*"
# Output: true
# Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

# Example 3:
# Input:
# s = "ab"
# p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".

# Example 4:
# Input:
# s = "aab"
# p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".

# Example 5:
# Input:
# s = "mississippi"
# p = "mis*is*p*."
# Output: false

class Solution:
    def isMatch(self, s, p):
        np=''
        for sp in p:                #这段代码是除去连续的*, 'a****b' --> 'a*b'
            if len(np) > 0 and np[-1] == sp == '*':
                continue
            else:
                np+=sp
        p=np

        lens = len(s)+1             #注意， 0 对应 字符串中-1索引，是空字符
        lenp = len(p)+1             #注意， 0 对应 字符串中-1索引，是空字符
        dp=[[None]*lenp for i in range(lens)]   #dynamic programming用的缓存, dp[i][j] 是 s[：i-1] 和 p[：j-1] 是否匹配
        dp[0][0]=True                   #0 索引是 空，对应 s[-1], p[-1], 所以如果 s='', p='',是匹配
        for i in range(1, lens):        #初始化dp[i][0] (i>0), 匹配(s[:i], p[-1])， 一定是False (非空串s 对 空p)
            dp[i][0] = False
        for j in range(1, lenp):        #初始化 dp[0][j], s=''
            if j==1 and p[0] == '*':    #p[0]=='*' 当 p是 '*W' 特殊情况, s='' 匹配 p[0]='*'
                dp[0][1] = True
            elif p[j-1] != '*':         #当 j>1 and p[j-1]!='*', s='' 一定不匹配 p[j-1]为有效字符（a-z)
                dp[0][j] = False
            else:                       #当 j>1 and p[j-1]=='*', 查看 j-2的状态， s='', p='acb*' =>  s='', p='ac'
                dp[0][j] = dp[0][j-2]
        #以上初始化完 i==0 or j==0 情况
        #以下是计算 i>0 and j>0 情况
        for i in range(1,lens):
            for j in range(1, lenp):
                if p[j-1] != '*':
                    dp[i][j] = dp[i-1][j-1] and (p[j-1]=='.' or s[i-1]==p[j-1])
                else:               
                    #P[j-1]=='*'， 比如 P[:j-1]='Wa*', P[j-1]=='*', P[j-2]=='a'
                    #一种可能是忽略 a*, 让 S[i-1] 去匹配 W=P[:j-3], 注意这里 dp对应的索引要+1, 是dp[i][j-2]
                    #一种可能是出现a大于等于1次的匹配， 让S[：i-2] 匹配 P[:j-1], 并且 S[i-1]=='a'==P[j-2] 以形成多次a去满足 'a*'这个条件
                    dp[i][j] = dp[i][j-2] or (j>1 and dp[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=='.'))
        return dp[lens-1][lenp-1]

#技术总结
#1.开始初始化 dp[0][*] 和 dp[*][0] 比较重要， 搞清楚 S='' 与 P=W , 和 S=A 与 P=''的匹配
#2.对于 P=Wa*这种情况， 分两种匹配，其中一种满足就行， case 1 match or case 2 match
# case 1 match 理解比较简单， 忽略'a*'后缀， 所以为 dp[i][j-2]
# case 2 match 复杂一些， 'a*' 匹配 'a' 或 'aa' 或 'aaa'..., 
# 所以 1. S[i-1]一定要等于'a'就是P[j-2]  (s[i-1]==p[j-2] or p[j-2]=='.'))
#     2. S[:i-2] 要 匹配 P[:j-1] (递归匹配)  (dp[i-1][j])
#3.整个过程贪婪的匹配过程，or 逻辑，只要有匹配就行， 不是最优化问题

s=Solution()
# print(s.isMatch('aab', 'c*a*b'))
print(s.isMatch('ab', '.*'))
print(s.isMatch("mississippi", "mis*is*p*."))
print(s.isMatch('a', 'a****'))






    
