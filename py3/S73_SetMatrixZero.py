'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

Follow up:

    A straight forward solution using O(mn) space is probably a bad idea.
    A simple improvement uses O(m + n) space, but still not the best solution.
    Could you devise a constant space solution?
'''

class Solution:
    def setZeroes(self, matrix):
        m=len(matrix)
        n=len(matrix[0])

        firstCol = False
        firstRow = False
        for i in range(0, m):
            if matrix[i][0] == 0:
                firstCol = True
                break
        for j in range(0, n):
            if matrix[0][j] == 0:
                firstRow = True
                break

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if firstCol:
            for i in range(0, m):
                matrix[i][0] = 0
        if firstRow:
            for j in range(0, n):
                matrix[0][j] = 0

s = Solution()
a=[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
s.setZeroes(a)
print(a)