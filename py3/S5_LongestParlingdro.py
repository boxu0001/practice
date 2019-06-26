# 5. Longest Palindromic Substring
# Medium

# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Example 2:

# Input: "cbbd"
# Output: "bb"

class Solution:
    def longestPalindromeDfs(self, s: str) -> str:
        lns= len(s)
        dp=[[False]*lns for i in range(lns)]    #用DFS 空间复杂度 O(nxn), 时间复杂度 O(nxn)
        maxSpan=0
        maxi=0
        maxj=0
        for sp in range(1, lns+1):              #但是遍历简单， 长度从 1 ～ lns, 注意 range的end是exclusive
            for i in range(0, lns-sp+1):    
                j=i+sp-1                        #确定好头尾索引， 就可以
                if sp==1:
                    dp[i][j]=True
                elif sp==2:
                    dp[i][j]=(s[i]==s[j])
                else:
                    dp[i][j] = dp[i+1][j-1] and (s[i]==s[j])

                if dp[i][j] and sp > maxSpan:
                    maxSpan=sp
                    maxi=i
                    maxj=j
        return s[maxi:maxj+1]


    def longestPalindromeExpanding(self, s: str) -> str:
        lns=len(s)
        maxi=0
        maxj=0
        maxLen=0
        #从中间开始， 注意奇偶
        i=0
        for i in range(lns):    
            if i >= lns - maxLen//2: #优化， 知道 maxLen, 可以缩小范围， i+MaxLenEven/2 < lns or i+MaxLenOdd//2 < lns
                continue
            for ei in [i, i+1]:     #odd, even
                si=i
                while lns > ei >= si >= 0 and s[si] == s[ei]:
                    if ei-si+1 > maxLen:
                        maxLen = ei-si+1
                        maxi=si
                        maxj=ei
                    ei+=1
                    si-=1
        return s[maxi:maxj+1]

    def longestPalindromePythonSpecific(self, s: str) -> str:
        maxl = 0
        start = 0
        for i in range(len(s)):
            if i - maxl >= 1 and s[i-maxl-1: i+1] == s[i-maxl-1: i+1][::-1]:    #这里用了python的数组反转 slice step， 速度较快
                start = i - maxl - 1
                maxl += 2
                continue
            if i - maxl >= 0 and s[i-maxl: i+1] == s[i-maxl: i+1][::-1]:
                start = i - maxl
                maxl += 1
        return s[start: start + maxl]


s=Solution()
print(s.longestPalindromePythonSpecific('abdbae'))