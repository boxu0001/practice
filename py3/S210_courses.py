'''
210. Course Schedule II
Medium

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .

Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .

Note:

    The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
    You may assume that there are no duplicate edges in the input prerequisites.

'''
from __future__ import annotations
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        m=[[] for _ in range(numCourses)]
        deps=[0] * numCourses
        for x,y in prerequisites:
            m[x]+=[y]
            deps[y]+=1
        result=[]
        visited=set({})
        for c in range(numCourses):
            if deps[c] == 0:
                stack=[[c,0]]
                onstack=set({c})
                while stack:
                    top, i = stack[-1]
                    if i >= len(m[top]):
                        stack.pop()
                        onstack.remove(top)
                        if top not in visited:
                            result+=[top]
                            visited.add(top)
                        
                        if stack:
                            stack[-1][1]+=1
                    else:
                        if m[top][i] in onstack:
                            return []
                        else:
                            stack+=[[m[top][i],0]]
                            onstack.add(m[top][i])
        
        return result if len(result) == numCourses else []
                
#another approach using queue with depth

s=Solution()
s.findOrder(8, [[1,0],[2,6],[1,7],[5,1],[6,4],[7,0],[0,5]])