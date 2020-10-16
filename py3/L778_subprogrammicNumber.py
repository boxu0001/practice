'''
776. Strobogrammatic Number II

Description

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
Find all strobogrammatic numbers that are of length = n.
Have you met this question in a real interview?  
Example

Example 1:

Input: n = 2, 
Output: ["11","69","88","96"]

Example 2:

Input: n = 1, 
Output: ["0","1","8"]

'''

class Solution:
    """
    @param n: the length of strobogrammatic number
    @return: All strobogrammatic numbers
    """
    def findStrobogrammatic(self, n):
        # write your code here
        f=[[] for _ in range(n+1)]
        f[0]=[""]
        if n > 0:
            f[1]=["0","1","8"]
        if n > 1:
            f[2]=["00","11","69","88","96"]
        for i in range(3, n+1):
            for x in f[i-2]:
                f[i]+=["0"+x+"0"]
            for x in f[i-2]:
                f[i]+=["1"+x+"1"]
                f[i]+=["6"+x+"9"]
                f[i]+=["8"+x+"8"]
                f[i]+=["9"+x+"6"]
        
        if n==0:
            return f[0]  
        elif n==1:
            return f[1]
        else:
            ls=len(f[n-2])  #注意对0的处理
            return f[n][ls:]
        
