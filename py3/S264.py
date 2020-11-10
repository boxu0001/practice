'''
264. Ugly Number II
Medium

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note:  

    1 is typically treated as an ugly number.
    n does not exceed 1690.
'''
import heapq as pq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        q=[1]
        res = 1
        qset=set({1})
        factors=[2,3,5]
        for i in range(n):
            res = pq.heappop(q)
            for f in factors:
                if res*f not in qset:
                    pq.heappush(q, res*f)
                    qset.add(res*f)
            
        return res
        