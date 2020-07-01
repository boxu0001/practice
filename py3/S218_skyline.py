# 218. The Skyline Problem

from __future__ import annotations

import heapq
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        bpq=sorted([[x, -h, y, True] for x, y, h in buildings] + [[y, h, y, False] for x, y, h in buildings])
        height=[[0, -1]]
        result=[[-1, 0]]
        for x, negh, y, left in bpq:
            if left:
                heapq.heappush(height, [negh, y])
            else:
                if y == height[0][1] and negh == -height[0][0]:
                    while  0 <= height[0][1] <= y:
                        heapq.heappop(height)

            if result[-1][1] != -height[0][0]:
                result += [[x, -height[0][0]]]
        return result[1:]
            
s=Solution()
r=s.getSkyline([[0,2,3],[2,5,3]])
print(r)