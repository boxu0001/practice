# 132. Palindrome Partitioning II
# Hard

# Given a string s, partition s such that every substring of the partition is a palindrome.

# Return the minimum cuts needed for a palindrome partitioning of s.

# Example:

# Input: "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

class Solution:
    def minCut(self, s: str) -> int:
        sl = len(s)
        r=[i-1 for i in range(sl+1)]    #初始化分割值， r[i] 为分割 长度 为i+1的子串s[:i+1]
        for i in range(sl):
            ii, jj = i, i
            while ii-1 >= 0 and sl >= jj+1 and s[ii-1] == s[jj]:    #even case
                ii -= 1
                jj += 1
                r[jj]=min(r[jj], r[ii]+1) #r[jj]为原有值， r[ii]+1为从分割两部分：s[:ii]， 和parlingdrom s[ii:jj]
                
            ii, jj = i+1, i
            while ii-1 >= 0 and sl >= jj+1 and s[ii-1] == s[jj]:    #odd case
                ii -= 1
                jj += 1
                r[jj]=min(r[jj], r[ii]+1)

        return r[sl]

s=Solution()
s.minCut('aab')

#总结
#1. 如果有parlingdrom, 使用parlingdrom, 
#2. 如果 s[i:j]是parlingdrom, r[j]取最小min（r[i]+1, r[j]）， 这里r[i]+1是 s[:i]分割数+1(s[i:j]是parlingdrom))
#注意r的初始化， 以及推演的过程