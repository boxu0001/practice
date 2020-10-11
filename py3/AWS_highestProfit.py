'''
Amazon Basics has several suppliers for its products. For each of the products, the stock is represented by a list of a number of items for each supplier. As items are purchased, the supplier raises the price by 1 per item purchased. Let's assume Amazon's profit on any single item is the same as the number of items the supplier has left. For example, if a supplier has 4 items, Amazon's profit on the first item sold is 4, then 3, then 2 and the profit of the last one is 1.

Given a list where each value in the list is the number of the item at a given supplier and also given the number of items to be ordered, write an algorithm to find the highest profit that can be generated for the given product.

Input
The input to the function/method consists on three arguments:

numSuppliers, an integer representing the number of suppliers;

inventory, a list of long integers representing the value of the item at a given supplier;

order, a long integer representing the number of items to be ordered.

Output

Return a long integer representing the highest profit that can be generated for the given product.

Constraints

1 <= numSuppliers <= 10^5

1 <= inventory[i] <= 10 ^ 5

0 <= i < numSuppliers

1 <= orders <= sum of inventory

Example1

Input:

numSuppliers = 2

inventory = [3,5]

order = 6

Output:

19

https://aonecode.com/amazon-online-assessment-amazon-find-the-highest-profit
'''

from __future__ import annotations
import heapq as pq
class Solution:
    def maxProfile(self, numSuppliers: int, inventory: list[int], order: int) -> int:
        profit=0
        queue=[]
        count={}
        for i in inventory:
            if i in count:
                count[i]+=1
            else:
                count[i]=1

        for p in count:
            pq.heappush(queue, [-p, count[p]]) #pass negtive for maxPQ
        
        while queue and order > 0:
            p, cnt = queue[0] #p is negtive here
            if order >= cnt:
                pq.heappop(queue)
                profit += (-p*cnt)
                order -= cnt

                nxtp = p+1  # nxtp is negtive
                if queue and queue[0][0] == nxtp:
                    queue[0][1]+=cnt
                elif nxtp < 0: #to make sure profitable
                    pq.heappush(queue, [nxtp, cnt])
                else:
                    pass

            else:
                profit += (-p*order)
                order = 0

        return profit


s=Solution()
s.maxProfile(0, [], 1)

# s.maxProfile(2, [3,5], 6)   #expect 19
# s.maxProfile(2, [2,5], 4) #expect 14
# s.maxProfile(5, [2, 8, 4, 10, 6], 20) #expect 110