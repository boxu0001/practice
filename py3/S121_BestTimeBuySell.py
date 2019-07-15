# 121. Best Time to Buy and Sell Stock
# Easy

# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.

# Example 1:

# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.

# Example 2:
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curBottom=None
        result=0
        for prc in prices:
            if curBottom == None or prc < curBottom:
                curBottom = prc
            else:
                if result < prc - curBottom:
                    result = prc-curBottom
        return result

#总结：
#低点买入，高点卖出
#保持curBottom为当前最低点，循环中，当前price要么成为最低点，要么有盈利，
#在有盈利的情况下，比较最大盈利