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
        s1=[s[i//2] if i&1==1 else '|' for i in range(0, len(s)*2+1)]
        # print(s1)
        f=[0]*(len(s)*2+1)
        calced=[False]*(len(s)*2+1)
        calced[0]=True
        maxd=0
        maxi=0
        for (cid, c) in enumerate(s1[1:]):
            if calced[cid] == True: 
                continue
            dist=1 if 1 > f[cid] else f[cid]
            while((not calced[cid]) and cid-dist>=0 and cid+dist<len(s1) and s1[cid-dist]==s1[cid+dist]):
                f[cid]=dist
                dist+=1
            calced[cid]=True
            if f[cid] > maxd:
                maxd=f[cid]
                maxi=cid
            lid=cid-f[cid]                  #left boundary index
            rid=cid+f[cid]                  #right boundary index
            for i in range(lid,cid):
                if i-f[i] > lid or (i-f[i] == lid and rid == len(s1)-1):
                    f[2*cid-i]=f[i]
                    calced[2*cid-i] = True
                elif i-f[i] < lid:
                    f[2*cid-i] = i - lid
                else:
                    f[2*cid-i] = f[i]
        # print(f)
        return s[(maxi-maxd)//2:(maxi+maxd)//2]
s=Solution()

print(s.longestPalindrome('babad'))
print(s.longestPalindrome('a'))
print(s.longestPalindrome('ab'))
print(s.longestPalindrome('abadedab'))

                
                
                


        

