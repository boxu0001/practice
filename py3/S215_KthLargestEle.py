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

#following are manually implemented Priority Queue
    def __init__(self):
        super().__init__()
        self.pq = []

    def pushPQ(self, ele):
        self.pq += [ele]
        self.pqUpLast()

    def popPQ(self):
        if len(self.pq) > 0:
            self.pq[0], self.pq[-1] = self.pq[-1], self.pq[0]
            first = self.pq.pop()
            self.pqDownFirst()
            return first
        else:
            return None

    def pqDownFirst(self):
        i = 0
        ls = len(self.pq)
        while i < ls:
            if 2*i+1 < ls:
                nxti = 2*i+1 if 2*i+2 >= ls or self.pq[2*i+2] < self.pq[2*i+1] else 2*i+2
                if self.pq[i] < self.pq[nxti]:
                    self.pq[i], self.pq[nxti] = self.pq[nxti], self.pq[i]
                    i = nxti 
                else:
                    return
            else:
                return


    def pqUpLast(self):
        ls = len(self.pq)
        i = ls-1
        pi = (i-1) >> 1
        while pi >= 0 and self.pq[i] > self.pq[pi]:
            self.pq[i], self.pq[pi] = self.pq[pi], self.pq[i]
            i = pi
        

#用priority queue 是核心        
s=Solution()
s.pushPQ(5)
s.pushPQ(3)
s.pushPQ(11)
s.pushPQ(9)
s.pushPQ(2)
s.pushPQ(7)

s.popPQ()
s.popPQ()
s.popPQ()
s.popPQ()
s.popPQ()

