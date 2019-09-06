'''
115. Distinct Subsequences
Hard

Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Example 1:

Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:

As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^

Example 2:

Input: S = "babgbag", T = "bag"
Output: 5
Explanation:

As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^

'''
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m=len(t)+1
        n=len(s)+1
        r=[[0]*n for _ in range(m)]
        for j in range(n):
            r[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                r[i][j] = (r[i-1][j-1] if t[i-1] == s[j-1] else 0) + r[i][j-1]
        return r[m-1][n-1]

# r(i,j):  1. if t[i-1]==s[j-1],加上 r(i-1, j-1), 
#          2. if t[i-1]!=s[j-1],算 r(i, j-1)
# 
# 核心为动态规划
# 注意初始化， r[0][j]=1 {for j in 0~n} , s[:x] 和 空串t[:0]都是匹配的(包括s[:0] 和 t[:0])， 反之则不行

