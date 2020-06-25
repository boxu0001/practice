'''
215. Kth Largest Element in an Array
Medium

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
'''
from __future__ import annotations
import heapq
class Solution:
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        ls=len(nums)
        sted={}
        pq=[]
        qi=0
        for n in nums:
            if n not in sted:
                sted[n]=1
                heapq.heappush(pq, -n)
            else:
                sted[n]+=1
        count=0
        while pq:
            nn=heapq.heappop(pq)
            count+=sted[-nn]
            if k<=count:
                return -nn
                
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq=[]
        for n in nums:
            heapq.heappush(pq, -n)
        for i in range(k-1):
            heapq.heappop(pq)
        return -heapq.heappop(pq)
#用priority queue 是核心        