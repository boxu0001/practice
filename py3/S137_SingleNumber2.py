'''
137. Single Number II
Medium

Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3

Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99
'''


from __future__ import annotations
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        for n in nums:
            three = twos & n
            twos |= ones & n
            ones ^= n
            
            ones &= ~three
            twos &= ~three
            print('{0:b} {1:b} {2:b}'.format(ones, twos, three))
        return ones

s=Solution()
s.singleNumber([0,1,0,1,0,1,99])
