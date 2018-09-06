# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.

# The matching should cover the entire input string (not partial).

# The function prototype should be:
# bool isMatch(const char *s, const char *p)

# Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "a*") → true
# isMatch("aa", ".*") → true
# isMatch("ab", ".*") → true
# isMatch("aab", "c*a*b") → true
class Solution:
    def isMatch(self, s, p):
        f=[[False] * (len(p)+1) for i in range(len(s)+1)]
        f[-1][-1]=True  #empty match empty
        for i in range(len(s), -1, -1):
            for j in range(len(p)-1, -1, -1):
                firstmatch = i < len(s) and p[j] in ('.', s[i])
                if j<len(p)-1 and p[j+1] == '*':
                    f[i][j] = firstmatch and f[i+1][j] or (f[i][j+2] and j<len(p)-1)
                elif firstmatch:
                    f[i][j] = f[i+1][j+1]
        return f[0][0]

    def isMatchCachedDP(self, text, pattern):
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans
            return memo[i, j]
        return dp(0, 0)

s=Solution()
print(s.isMatch("aa", "*"))
print(s.isMatch("aa", "aa"))
print(s.isMatch("aaa", "aa"))
print(s.isMatch("aa", "a*"))
print(s.isMatch("ab", ".*"))
print(s.isMatch("aab", "c*a*b"))