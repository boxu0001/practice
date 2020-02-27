from __future__ import annotations
'''
162. Find Peak Element
Medium

A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.
'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for idx, mid in enumerate(nums):
            if (idx == 0 or mid > nums[idx-1]) and (idx == len(nums)-1 or mid > nums[idx+1]):
                return idx

        return None

    def findPeakElementBin(self, nums: List[int]) -> int:
        ln=len(nums)
        s=0
        e=ln-1
        while s <= e:
            m = (s+e)//2
            if (m == 0 or nums[m-1] < nums[m]) and (m == ln-1 or nums[m+1] < nums[m]):
                return m
            elif m < ln -1 and nums[m+1] > nums[m]:
                s = m+1
            else:
                e = m
        return None

s=Solution()
s.findPeakElementBin([1])