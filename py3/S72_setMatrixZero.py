# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

# Example 1:

# Input: 
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# Output: 
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]

# Example 2:

# Input: 
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# Output: 
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]

# Follow up:

#     A straight forward solution using O(mn) space is probably a bad idea.
#     A simple improvement uses O(m + n) space, but still not the best solution.
#     Could you devise a constant space solution?

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0]) if m > 0 else 0
        firstRow0=False
        firstCol0=False
        for j in range(n):
            if matrix[0][j]==0:
                firstRow0=True
                break        
        for i in range(m):
            if matrix[i][0]==0:
                firstCol0=True
                break
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        for i in range(1, m):
            if matrix[i][0] == 0:
                matrix[i] = [0]*n
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        if firstRow0:
            matrix[0] = [0] * n
        if firstCol0:
            for i in range(m):
                    matrix[i][0] = 0
            
        
#注意：
#1. 要达到O(1)的空间复杂度，把第一行和第一列作为存储
#2. 查看第一行第一列是否含有0
#3. 遍历(1,m)行， （1,n)列，set 0 on 第一行，第一列
#4. 根据第一行列，set 0
#5. 第一行和第一列要最后设置0