'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.

Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true

Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
'''

import bisect
import numpy as np

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m=len(matrix)
        if m == 0 or len(matrix[0]) == 0:
            return False
        n=len(matrix[0])
        start,end=0, m*n-1
        while(0<= start <= end < m*n):
            mid=(start+end)>>1 
            test=matrix[mid//n][mid%n]
            if test == target:
                return True
            elif test < target:
                start = mid+1
            else:
                end = mid-1
        return False


s = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]


print(s.searchMatrix(matrix, 3))