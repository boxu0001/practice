'''
48. Rotate Image
Medium

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

Example 2:
Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
'''
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        r4=n//2             #consider n is even/odd, for the top-left part rows, eg n=4 or 5, rows=2, it will iterate 0, 1
        c4=(n+1)//2         #consider n is even/odd, for the top-left part columns, eg n=4, rows=2(iterate 0, 1); n=5, rows=3(iterate 0, 1, 2)
        for i in range(r4):
            for j in range(c4):
                tmp=matrix[i][j]
                matrix[i][j] = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = tmp

# summary:
# 1. matrix[i][j] -> matrix[j][n-1-i] -> matrix[n-1-i][n-1-j] -> matrix[n-1-j][i] -> matrix[i][j]
# 2. only need to loop 1/4 elements of the matrix, here it's the top-left 1/4 part.
# 还有另外一种解法， 先对角线翻转，然后中线上下翻转


s=Solution()
m1=[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
s.rotate(m1)
print(m1)
m2=[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
s.rotate(m2)
print(m2)