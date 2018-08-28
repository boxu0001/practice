'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:

Input: m = 7, n = 3
Output: 28
'''

class Solution:
    def uniquePaths(self, m, n):
        #C(m+n-2, m-1)
        pm,pn,pmn=1,1,1
        for i in range(1, m+n-1):
            pmn*=i
            if i==m-1:
                pm=pmn
            if i==n-1:
                pn=pmn
        return pmn//(pm*pn)

    def uniquePaths2(self, m, n):
        #C(m+n-2, m-1)
        t,s=1,1
        k=min(m,n)-1
        for i in range(m+n-2,m+n-2-k,-1):
            t*=i
        for i in range(1,k+1):
            s*=i
        return t//s

    #dynamic programming
    def uniquePathsDP(self, m, n):
        #C(m+n-2, m-1)=C(m+n-1, m-1)+C(m+n-1, m-2)
        s=min(m,n)-1
        t=m+n-2
        c=[[1, i] + [0]*s for i in range(t+1)]
        for si in range(1, s+1):
            for ti in range(2, t+1):
                c[ti][si]=c[ti-1][si]+c[ti-1][si-1]
        return c[t][s]


s=Solution()        
print(s.uniquePaths2(200,100))
print(s.uniquePaths(200,100))

        