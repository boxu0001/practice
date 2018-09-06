# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

# Your algorithm's runtime complexity must be in the order of O(log n).

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

class Solution:
    def search(self, nums, target):
        ls = len(nums)
        result = -1
        if ls == 0:
            return result
        start = 0
        end = ls-1
        biStart = 0
        if nums[0] > nums[ls-1]:
            biEnd = ls - 1
            biMid = (biStart+biEnd)//2
            while biMid > biStart:
                if nums[biMid] > nums[biStart]:
                    biStart = biMid
                else:
                    biEnd = biMid
                biMid = (biStart+biEnd)//2
            start = 0 if target >= nums[0] else biEnd
            end = ls-1 if target <= nums[ls-1] else biStart
        while(start <= end):
            mid = (start+end)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                end = mid-1
            else:
                start = mid+1
        return result        

s=Solution()
print(s.search([4,5,6,7,0,1,2], 0))
print(s.search([4,5,6,7,0,1,2], 3))
print(s.search([5], 2))