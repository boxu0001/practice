'''
1091. Shortest Path in Binary Matrix
Medium

In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

    Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
    C_1 is at location (0, 0) (ie. has value grid[0][0])
    C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
    If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).

Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.

 

Example 1:

Input: [[0,1],[1,0]]


Output: 2

Example 2:

Input: [[0,0,0],[1,1,0],[1,1,0]]


Output: 4

 

Note:

    1 <= grid.length == grid[0].length <= 100
    grid[r][c] is 0 or 1

'''
from __future__ import annotations

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N=len(grid)
        pq=[[0, 0]] if N > 0 and grid[0][0] == 0 else []
        visited={0:1} if N > 0 and grid[0][0] == 0 else []
        while pq:
            x,y = pq.pop(0)
            d = visited[x*N+y]
            for i in range(-1,2):
                for j in range(-1,2):
                    nx = x+i
                    ny = y+j
                    nxy = nx*N+ny
                    if 0<=nx<N and 0<=ny<N and nxy not in visited and grid[nx][ny] == 0:
                        pq+=[[nx, ny]]
                        visited[nxy]=d+1
                
        target = (N-1)*(N+1)
        if target in visited:
            return visited[target]
        else:
            return -1

#简化版的shortest path 问题，不需要用到priority queue, 因为bfs所有路径为最短路经,只需用queue就行

s= Solution()
# s.shortestPathBinaryMatrix(([[0,0,1,1,0,0],[0,0,0,0,1,1],[1,0,1,1,0,0],[0,0,1,1,0,0],[0,0,0,0,0,0],[0,0,1,0,0,0]]))
s.shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]])
