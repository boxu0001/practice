'''
188. Best Time to Buy and Sell Stock IV
Hard

Say you have an array for which the i-th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:

Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

'''
from __future__ import annotations
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        trx = []
        startP=prices[0]
        endP=None
    
        #简化可行交易
        for i in range(1, len(prices)):
            if prices[i] >= prices[i-1]:
                endP = prices[i]
            else:
                if endP != None:
                    trx+=[startP, endP]
                    endP = None
                startP = prices[i]
        if endP != None:
            trx+=[startP, endP]

        # 
        #   f[d, start] = max of following:
        #           f[d, start+1]   ---> from trx[start+1], needs "d" transactions
        #           f[d-1, start+1]   ---> from trx[start+1], needs "d-1" transactions
        #           f[d-1, start+2]   ---> from trx[start+2], needs "d-1" transactions
        #           f[d-1, start+3]   ---> from trx[start+3], needs "d-1" transactions
        #              ...
        #           f[d-1, n-1]   ---> from trx[n], needs "d-1" transactions, n is beyond the boundary, set as 0 always
        #

        n=len(trx)
        if k >= n//2:
            return sum(trx[i+1] - trx[i] for i in range(0, n-1, 2))
        
        f=[[0]*(n+1) for _ in range(k+1)]

        # 这里tmp[d][i]是存 max(f[d][j]+trx[j]) i <= j <= n-1, 所以 f[d][i]=tmp[d-1][i+1] - trx[i], 用来辅助和优化
        # 初始化 f[0][*] = 0, f[*][n] = 0
        # 初始化 tmp[0][i from 0 to n-1] = max(trx[i], trx[i+1], ... trx[n-1]), tmp[*][n] = 0
        tmp=[[0]*(n+1) for _ in range(k+1)] 
        for i in range(n-1, -1, -1):
            tmp[0][i] = max(tmp[0][i+1], trx[i])

        for d in range(1, k+1):
            for i in range(n-2, -1, -1): #from n-2 to 0
                f[d][i] = max(f[d][i+1], tmp[d-1][i+1] - trx[i])
                tmp[d][i] = max(tmp[d][i+1], f[d][i]+trx[i])
        return f[k][0]

s=Solution()
s.maxProfit(2,[3,3,5,0,0,3,1,4])
