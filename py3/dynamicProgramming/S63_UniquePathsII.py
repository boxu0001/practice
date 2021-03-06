'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.
Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
'''
class Solution:
	def uniquePathsWithObstacles(self, obstacleGrid):
		m=len(obstacleGrid)
		n=len(obstacleGrid[0]) if m > 0 else 0
		for i in range(m):
			for j in range(n):
				if obstacleGrid[i][j] == 1:
					obstacleGrid[i][j] = 0
				elif i==0 and j == 0:
					obstacleGrid[i][j]=1
				else:
					obstacleGrid[i][j]=(obstacleGrid[i-1][j] if i > 0 else 0) + (obstacleGrid[i][j-1] if j > 0 else 0)				
		return obstacleGrid[-1][-1]

s=Solution()
print(s.uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
]))