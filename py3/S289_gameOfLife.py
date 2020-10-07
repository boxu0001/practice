'''
289. Game of Life
Medium

According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

    Any live cell with fewer than two live neighbors dies, as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population..
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]

Follow up:

    Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
    In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

'''

from __future__ import annotations
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        M=len(board)
        N=len(board[0]) if M > 0 else 0
        updated=[]
        dir8=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        for i in range(M):
            for j in range(N):
                cnt = 0
                for di, dj in dir8:
                    x=i+di
                    y=j+dj
                    if 0<=x<M and 0<=y<N:
                        cnt+=board[x][y]
                if (board[i][j] == 1 and (cnt < 2 or cnt > 3)) or (board[i][j] == 0 and cnt == 3):
                    updated+=[(i,j)]
        
        for x,y in updated:
            board[x][y] = board[x][y]^1

    def gameOfLifeInplace(self, board: List[List[int]]) -> None:
        M=len(board)
        N=len(board[0]) if M > 0 else 0
        dir8=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        for i in range(M):
            for j in range(N):
                cnt = 0
                for di, dj in dir8:
                    x=i+di
                    y=j+dj
                    if 0<=x<M and 0<=y<N:
                        cnt+=board[x][y] & 1    # in binary XY & 1 == Y

                if (board[i][j] == 1 and (cnt < 2 or cnt > 3)):
                    board[i][j] = 3     #last bit represent the original value
                if (board[i][j] == 0 and cnt == 3):
                    board[i][j]= 2      #in binary, 3 means from '1' to '0'; 2 means from '0' to '1'
        for x in range(M):
            for y in range(N):
                if board[x][y] >= 2:
                    board[x][y] = 3 - board[x][y]


s=Solution()
s.gameOfLifeInplace([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])


                


