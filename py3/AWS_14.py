from __future__ import annotations
import heapq as pq
class Solution:
    def schedule(self, ability: list[int], processes: int) -> int:
        queue=[]
        for ab in ability:
            pq.heappush(queue, -ab)
        
        time = 0
        while processes > 0:
            negtiveAb = pq.heappop(queue)
            ab = -negtiveAb
            processes -= ab
            time+=1
            ab = ab//2
            pq.heappush(queue, -ab)

        return time


s=Solution()
s.schedule([5,9,10,3], 30)








