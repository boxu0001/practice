'''
994. Rotting Oranges
Medium

In a given grid, each cell can have one of three values:

    the value 0 representing an empty cell;
    the value 1 representing a fresh orange;
    the value 2 representing a rotten orange.

Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

Example 1:

Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.

Note:

    1 <= grid.length <= 10
    1 <= grid[0].length <= 10
    grid[i][j] is only 0, 1, or 2.

'''

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M = len(grid) if grid else 0
        N = len(grid[0]) if M > 0 else 0
        
        queue = []
        fresh=0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 2:
                    queue += [(i,j)]
                if grid[i][j] == 1:
                    fresh+=1
        
        hours = 0
        fourdir = [(1,0), (-1,0), (0,1), (0,-1)]
        while queue:
            nxtlist = []
            for (x,y) in queue:
                for (i,j) in fourdir:
                    nx = x+i
                    ny = y+j
                    if 0<=nx<M and 0<=ny<N and grid[nx][ny] == 1:
                        grid[nx][ny]=2
                        nxtlist+=[(nx,ny)]
                        fresh-=1
            if nxtlist:
                hours+=1
                
            queue=nxtlist
        
        #注意edge case, 只要有没坏的，就是-1,其它按时间来算
        return hours if fresh == 0 else -1
    