'''
207. Course Schedule
Medium

There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.

 

Constraints:

    The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
    You may assume that there are no duplicate edges in the input prerequisites.
    1 <= numCourses <= 10^5

'''
from __future__ import annotations
class Solution:

    def canFinishByQueue(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        m={}
        deps=[0]*numCourses     #这里用depth来计算cycle,
        for x,y in prerequisites:
            if x not in m:
                m[x] = [y]
            else:
                m[x]+=[y]
            deps[y]+=1
        queue=[]
        for x in m.keys():
            if deps[x] == 0:    #所有的根都是depth=0， 所有的depth=0一定是根
                queue+=[x]
        while queue:
            top = queue.pop(0)
            if top in m:
                for y in m[top]:
                    deps[y]-=1  # cycle一定是负
                    if deps[y] == 0:
                        queue+=[y]
        return sum(deps) == 0

    def canFinishByStack(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        m={}
        visited=set({})
        
        for x,y in prerequisites:
            if x not in m:
                m[x] = [y]
            else:
                m[x]+=[y]
        for x in m.keys():
            if x not in visited:
                stack=[[x,0]]
                keyset=set({x})
                while stack:
                    key, i = stack[-1]
                    if i < len(m[key]):
                        nxt=m[key][i]
                        if nxt in visited or nxt not in m:  #visited or leaf
                            stack[-1][1]+=1
                        elif nxt not in keyset:     #not in cycle
                            stack+=[[nxt, 0]]
                            keyset.add(nxt)    
                        else:                       # in cycle
                            return False
                    else:
                        stack.pop()     #key is visited
                        keyset.remove(key)
                        visited.add(key)
            
        return True

s=Solution()
s.canFinishByQueue(5, [[2,1], [1,0]])