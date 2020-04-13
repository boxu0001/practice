##### deprecated problem ######

'''
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4

Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6

'''

from __future__ import annotations
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        lines={} #map of point set and its tan
        dup = {}
        for (x, y) in points:
            if (x, y) not in dup:
                dup[(x,y)] = 1
            else:
                dup[(x,y)]+=1
        
        points = list(dup.keys())
        ls=len(points)
        
        for i in range(ls):
            for j in range(i+1, ls):
                pix, piy = points[i]
                pjx, pjy = points[j]
                
                added=False
                for lKey in lines.keys():
                    line = lines[lKey]
                    if points[i] in line and points[j] in line:
                        added = True
                        break
                    elif points[i] in line and points[j] not in line:
                        tan = (piy-pjy)/(pix-pjx) if pix != pjx else 'INF'
                        _, tt = lKey
                        if tan == tt:
                            lines[lKey].add(points[j])
                            added = True
                            break
                    else:
                        pass
                    
                if not added:
                    tan = (piy-pjy)/(pix-pjx) if pix != pjx else 'INF'
                    lines[(i, tan)] = set({points[i], points[j]})
                    
        result = max(dup.values())
        for line in lines.values():
            r = 0
            for p in line:
                r += dup[p]
            result = max(r, result)
        
        return result

s=Solution()
s.maxPoints([[1,1], [2,2], [3,3]])
