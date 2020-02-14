'''
152. Maximum Product Subarray
Medium

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return None
        result = nums[0]
        curmax = nums[0]
        curmin = nums[0]
        
        for v in nums[1:]:
            nxtmax = max(curmax * v, curmin * v, v)     #对于每一个数， 计算包含这个数的最大值， 这个值有可能对下一个数形成潜在最大值
            nxtmin = min(curmax * v, curmin * v, v)     #对于每一个数， 计算包含这个数的最小值， 这个值有可能对下一个数形成潜在最大值
            result = max(result, nxtmax)                
            curmax = nxtmax
            curmin = nxtmin
            
        return result

#考虑其他形式的问题，eg. 最大连续求和