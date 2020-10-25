'''
934. Shortest Bridge
Medium

In a given 2D binary array A, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)

 

Example 1:

Input: A = [[0,1],[1,0]]
Output: 1

Example 2:

Input: A = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2

Example 3:

Input: A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1

 

Constraints:

    2 <= A.length == A[0].length <= 100
    A[i][j] == 0 or A[i][j] == 1
'''
from __future__ import annotations
class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        R=len(A)
        C=len(A[0]) if R > 0 else 0
        
        island1=None
        bdr1=set({})
        dirs=[(1,0),(-1,0),(0,1),(0,-1)]

        #find island and its boundary   
        for i in range(R):
            for j in range(C):
                if A[i][j] == 1:
                    island1={(i,j)}
                    queue=[(i,j)]
                    while queue: # Time: O(RxC), Space: O(RxC)
                        x,y=queue.pop()
                        for dx, dy in dirs:
                            if 0<=x+dx<R and 0<=y+dy<C:
                                if A[x+dx][y+dy] == 1 and (x+dx, y+dy) not in island1:
                                    island1.add((x+dx, y+dy))
                                    queue+=[(x+dx, y+dy)]
                                
                                if A[x+dx][y+dy] == 0 and (x+dx, y+dy) not in bdr1:
                                    bdr1.add((x+dx, y+dy))
                                
                    break
            if island1 != None:
                break

        
        #bfs expand boundary, Time: O(RxC), Space: O(RxC)
        count=0
        qb=list(bdr1)
        while qb:
            count+=1
            
            tmp=[]
            for x, y in qb:
                for dx, dy in dirs:
                    if 0<=x+dx<R and 0<=y+dy<C:
                        if A[x+dx][y+dy] == 1 and (x+dx, y+dy) not in island1:
                            return count
                        if A[x+dx][y+dy] == 0 and (x+dx, y+dy) not in bdr1:
                            bdr1.add((x+dx, y+dy))
                            tmp+=[(x+dx,y+dy)]  
            qb=tmp
            
        return count   
        
s=Solution()                            
s.shortestBridge([[0,0,0,0,0,0],[0,1,0,0,0,0],[1,1,0,0,0,0],[1,1,0,0,0,0],[0,0,0,0,0,0],[0,0,1,1,0,0]])
                        
                        
                    
                    