'''
343. Integer Break
Medium

Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

Example 1:

Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.

Example 2:

Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.

Note: You may assume that n is not less than 2 and not larger than 58.
'''

import heapq 
class Solution:

    def integerBreak(self, n: int) -> int:
        result = 1
        for i in range(n//2， 1， -1):     #用抽屉原理，等分成 i 个抽屉
            m, k = divmod(n, i)                 #每个抽屉基本的分配数量， 还要考虑多余的叠加
            tmp = m**(i-k)*(m+1)**k
            if tmp > result:
                result = tmp
            else:
                break
        return result

    def integerBreak2(self, n: int) -> int: #本方法用priority queue
        cnt, rem = divmod(n,2)
        queue=[2]*cnt
        heapq.heapify(queue)
        if rem > 0:
            heapq.heappush(queue, rem)
        result = 1
        
        while len(queue) > 1:
            tmp = 1
            for x in queue:
                tmp*=x
                
            if tmp > result:
                result = tmp
            else:
                break
        
            smallest = heapq.heappop(queue)
            if queue:    
                for _ in range(smallest):
                    top = queue[0]
                    heapq.heapreplace(queue, top+1)
                
        return result



