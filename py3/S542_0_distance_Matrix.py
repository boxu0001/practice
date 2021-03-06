'''
542. 01 Matrix
Medium

Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]

Note:

    The number of elements of the given matrix will not exceed 10,000.
    There are at least one 0 in the given matrix.
    The cells are adjacent in only four directions: up, down, left and right.
'''

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        M=len(matrix)
        N=len(matrix[0])
        result=[[None]*N for _ in range(M)]
        queue=[]
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    result[i][j] = 0
                    queue+=[(i,j)]
        
        d4=[(1,0),(-1,0),(0,1),(0,-1)]
        while queue:        #queue 中的距离值 为[0...0, 1...1, 2...2, ...]
            x,y = queue.pop(0)
            for dx, dy in d4:
                nx=x+dx
                ny=y+dy
                if 0<=nx<M and 0<=ny<N and result[nx][ny] == None:
                    result[nx][ny] = result[x][y]+1
                    queue+=[(nx, ny)]
                    
        return result
#继续优化可以不用result, 直接用matrix