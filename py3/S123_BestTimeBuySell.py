# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete at most two transactions.
# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

# Example 1:
# Input: [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
#              Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

# Example 2:
# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
#              Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
#              engaging multiple transactions at the same time. You must sell before buying again.

# Example 3:
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result=0
        ls=len(prices)
        fLeft=[0]*ls
        fRight=[0]*ls
        leftMin=prices[0] if ls > 0 else None
        rightMax=prices[-1] if ls > 0 else None
        for i in range(1, ls):
            if prices[i] <= prices[i-1]:
                fLeft[i] = fLeft[i-1]
                leftMin = min(leftMin, prices[i])
            else:
                fLeft[i] = max(fLeft[i-1], prices[i]-leftMin)
                
            j=ls-1-i
            if prices[j] >= prices[j+1]:
                fRight[j] = fRight[j+1]
                rightMax = max(rightMax, prices[j])
            else:
                fRight[j] = max(fRight[j+1], rightMax-prices[j])
            
        for s in range(ls):
            result=max(result, fLeft[s]+fRight[s])
            
        return result

    def maxProfit2(self, prices: List[int]) -> int:
        mx1=[0]     #mx1 数组存第i个元素之前的最大值获利值，所以mx1[0]为0（没开始交易），mx1[1]也会为0（只有i==0这个交易起点）
        newLow=prices[0] if prices else None
        mx1gain=0
        for p in prices:
            if p > newLow:
                mx1gain = p-newLow if p-newLow > mx1gain else mx1gain
            else:
                newLow = p
            mx1+=[mx1gain]
        newHigh=prices[-1] if prices else None
        result=mx1gain
        mx2gain=0
        for qi in range(len(prices)-1, -1, -1):
            if prices[qi] < newHigh:
                mx2gain = newHigh - prices[qi] if newHigh - prices[qi] > mx2gain else mx2gain
            else:
                newHigh = prices[qi]
            if mx2gain + mx1[qi] > result:      #mx2gain为从qi为起点的最大值， mx1[qi]为qi点之前的最大值（不包括qi点）
                result = mx2gain + mx1[qi]
            
        return result

#总结：
#分析中，有至少两次交易所产生的最佳结果， 一次交易 vs 两次交易
#1. 很容易证明最佳交易一定是可拆分成两次交易（不失一般性，定义在数组之前和之后的价格为, price_before=prices[0], price_after=prices[-1]）
#2. best_result=best_result_before[i]+best_result_after[i], both inclusive i, 
#   这样找到在i点左边（包括i)的最佳交易，和i点右边（包括i)的最佳交易， 两者之和 为可能的最佳交易
#3. 这里用了dynamic programming里的缓存，fLeft and fRight, fLeft为在i点左侧的最佳交易值， fRight为在i点右侧的最佳交易值，
#   对于i左边的最佳交易，如果 prices[i] < prices[i-1], 那么 fLeft[i]一定等于fLeft[i-1],因为i点为低位，不能形成更好的盈利卖出点；
#   但是i点可以成为潜在的买入点： leftMin = min(leftMin, prices[i]); 
#   对于i右边的最佳交易，如果 prices[j] >= prices[j+1], 那么 fRight[j]一定等于fRight[j+1],因为j点为高位，不能形成更好的买入点让j右边形成更大的盈利；
#   但是j点可以成为潜在的卖出点： rightMax = max(rightMax, prices[j]); 