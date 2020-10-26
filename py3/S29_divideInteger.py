# 29. Divide Two Integers
# Medium

# Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

# Return the quotient after dividing dividend by divisor.

# The integer division should truncate toward zero.

# Example 1:
# Input: dividend = 10, divisor = 3
# Output: 3

# Example 2:
# Input: dividend = 7, divisor = -3
# Output: -2

# Note:
#     Both dividend and divisor will be 32-bit signed integers.
#     The divisor will never be 0.
#     Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2**31,  2**31 − 1]. 
# For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = (1<<31)-1
        MIN_INT = -1<<31
        isPositive = not((dividend > 0) ^ (divisor > 0))
        x=abs(dividend)
        y=abs(divisor)
        
        f=[(0,0), (y,1)]    #f[i] ==> (count*y, count)
        i=1
        while f[i][0] < x:
            cy, c = (f[i][0] + f[i-1][0], f[i][1] + f[i-1][1])
            f+= [(cy,c)]
            i+=1
        i=len(f)-1
        count=0
        while x >= y:
            if x >= f[i][0]:
                count+=f[i][1]
                x-=f[i][0]
            i-=1
        
        count = count if isPositive else -count
        return count if MAX_INT >= count >= MIN_INT else MAX_INT
#key part is that using Fibonacci series
#if f[i+1]>x>=f[i], then f[i-1]>x-f[i]>=0

s=Solution()
print(s.divide(100,24))