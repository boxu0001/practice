'''
688. Knight Probability in Chessboard
Medium

On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves. The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

 

 

Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.

 

Example:

Input: 3, 2, 0, 0
Output: 0.0625
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.

'''

from __future__ import annotations
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        if K == 0:
            return 1
        
        #the first move
        moves=[[-1,-2],[-1,2],[1,-2],[1,2],[-2,-1],[-2,1],[2,-1],[2,1]]
        count=None

        for d in range(K-1):
            nxtcount=[[0]*N for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    for [x,y] in moves:
                        if 0<=i+x<N and 0<=j+y<N:
                            nxtcount[i][j]+=count[i+x][j+y] if count else 1
            count = nxtcount

        if count:
            res = sum([count[r+x][c+y] for [x, y] in moves if 0<=r+x<N and 0<=c+y<N ])
        else:
            res = sum([1 for [x, y] in moves if 0<=r+x<N and 0<=c+y<N ])

        return res/(8**K)

#f(n)(t) = f[n-1][a] + f[n-1][b] + .... , t next valid moves are a, b, ...

s=Solution()
# s.knightProbability(3, 2, 0, 0)
s.knightProbability(3, 3, 0, 0)
# s.knightProbability(8, 2, 0, 0)