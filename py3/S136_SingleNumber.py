# 136. Single Number
# Easy
# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Example 1:
# Input: [2,2,1]
# Output: 1

# Example 2:
# Input: [4,1,2,1,2]
# Output: 4

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        r=0
        for i in nums: r^=i
        return r

#注意， 
#1. 用到XOR操作
#2. 0 ^ N = N
#3. A XOR B = (A | B) & (~A | ~B)