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
            mi = (si + ei)//2       # 这里//2是向小的index靠近的，例如 （3+4）// 2 == 3， 所以有下一步的ei=mi, 不是ei=mi-1
            if nums[mi] < nums[ei]: # compare with end, if middle < end, then from mi -> ei is ascending, and minimal is in si -> mi range
                ei = mi
            else:                   # else, there is a break point and minimal is in the range
                si = mi+1    
            
        if result == None:
            result = nums[si]
        return result


    def findMin2(self, nums: List[int]) -> int:
        si, ei = 0, len(nums)-1
        result = None
        while si < ei:
            mi = (si + ei)//2 + 1   # 这里//2是向小的index靠近, +1 向大的index靠近
            if nums[mi] < nums[si]: # compare with start
                ei = mi
            else:                   # else, there is a break point and minimal is in the range
                si = mi+1           # mi is not, as nums[mi] > nums[si] > smallest, so mi+1 is potential
            
        if result == None:
            result = nums[si]
        return result


# consider corner cases:
# [3] or [2, 4] or [4, 2]