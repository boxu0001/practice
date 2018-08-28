# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
# Example:
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Example:
# Input: "cbbd"
# Output: "bb"
#Manacher's Algo
class Solution:
    def longestPalindrome(self, s):
        maxLen=1
        maxs=s[0]
        for i in range(1, len(s)):
            left1=i-maxLen if i-maxLen > 0 else 0
            left2=i-maxLen-1 if i-maxLen-1>0 else 0
            si1=s[left1:i+1]
            si2=s[left2:i+1]
            if si1 == si1[::-1] and i+1-left1 > maxLen:
                maxLen = i+1-left1
                maxs=si1
            if si2 == si2[::-1] and i+1-left2 > maxLen:
                maxLen = i+1-left2
                maxs=si2
        return maxs

    def longestPalingdromeWithDP(self, s):
        ls=len(s)
        if ls == 0:
            return ""
        maxl = 1
        maxStr = s[0]
        for i in range(2*ls-1):
            l = 1 if i % 2 == 0 else 0
            si, ei = (i+1)//2-1, i//2+1
            while ls > ei and si >= 0: 
                if s[si] == s[ei]:
                    si-=1
                    ei+=1
                else:
                    break
            if ei - si - 1 > maxl:
                maxStr = s[si+1:ei]
                maxl = ei - si - 1
        return maxStr

s=Solution()

# print(s.longestPalindrome('babad'))
# print(s.longestPalindrome('aa'))
# print(s.longestPalindrome('ab'))
# print(s.longestPalindrome('abadedab'))
# print(s.longestPalingdromeWithDP('babad'))
# print(s.longestPalingdromeWithDP('aa'))
print(s.longestPalingdromeWithDP('a'))
# print(s.longestPalingdromeWithDP('abadedab'))      
                
                


        

