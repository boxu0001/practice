'''
221. Maximal Square
Medium

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
'''
from __future__ import annotations
class Solution:
    #using DP, O(log(n**2)), but only using one storage
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0]) if m > 0 else 0
        
        res = 0
        r = [[0]*n for _ in range(m)] # r[i][j] counting the square side length with (i,j) as bottom right

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i==0 or j==0:
                        r[i][j] = 1
                    else:
                        r[i][j] = min(r[i-1][j-1], r[i-1][j], r[i][j-1]) + 1    
                        #以上的比较理解为取两翼最小值，再比较缩小一层的区域

                    res = max(res, r[i][j])

        return res*res

    #using DP, O(log(n**2))
    def maximalSquare1(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0]) if m > 0 else 0
        
        res = 0
        r = [[0]*n for _ in range(m)] # r[i][j] counting the square side length with (i,j) as bottom right
        l = [[0]*n for _ in range(m)] # l[i][j], to the left and including (i,j), the consecutive "1" numbers
        u = [[0]*n for _ in range(m)] # l[i][j], to the upper and including (i,j), the consecutive "1" numbers

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    l[i][j] = (1+l[i][j-1]) if j-1>=0 else 1
                    u[i][j] = (1+u[i-1][j]) if i-1>=0 else 1
                    r[i][j] = min(r[i-1][j-1]+1, l[i][j], u[i][j]) if i-1>=0 and j-1>=0 else 1
                    res = max(res, r[i][j])

        return res*res

    #O(log(n**3))
    def maximalSquare2(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0]) if m > 0 else 0
        mn = min(m, n)
        result=0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != '0':
                    r = 1
                    x = i+1
                    y = j+1
                    while x < m and y < n and matrix[x][y] =='1':
                        valid = True
                        for d in range(0, x-i):
                            if matrix[x][j+d] == '0' or matrix[i+d][y] == '0':
                                valid = False
                                break
                        if valid:
                            r+=1
                            x+=1
                            y+=1
                        else:
                            break
                    if r > result:
                        result = r
        
        return result**2



d=Solution()
d.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])