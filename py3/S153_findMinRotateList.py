'''
153. Find Minimum in Rotated Sorted Array
Medium

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1

Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        si, ei = 0, len(nums)-1
        result = None
        while si < ei:
            mi = (si + ei)//2
            if nums[mi] < nums[ei]: # if middle < end, then from mi -> ei is ascending, and minimal is in si -> mi range
                ei = mi
            else:                   # else, there is a break point and minimal is in the range
                si = mi+1    
            
        if result == None:
            result = nums[si]
        return result
# consider corner cases:
# [3] or [2, 4] or [4, 2]