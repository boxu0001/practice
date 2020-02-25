'''
154. Find Minimum in Rotated Sorted Array II
Hard

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1

Example 2:

Input: [2,2,2,0,1]
Output: 0
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        si = 0
        ei = len(nums)-1
        while si < ei:
            mi = (si + ei) // 2
            if nums[mi] > nums[ei]:
                si = mi + 1
            elif nums[mi] < nums[ei]:
                ei = mi
            elif nums[mi] > nums[si]:
                return nums[si]
            elif nums[mi] < nums[si]:
                ei = mi
                si = si + 1
            else:   #nums[si] == nums[mi] == nums[ei]
                ei-=1
                si+=1
        return nums[si]

    def findMinImproved(self, nums: List[int]) -> int:
        si = 0
        ei = len(nums) -1
        
        while si < ei:
            if nums[si] < nums[ei]:
                return nums[si]
            mi = (si+ei)//2
            if nums[mi] > nums[ei]:
                si = mi + 1
            elif nums[mi] < nums[ei]:
                ei = mi
            else:
                ei-=1
        return nums[si]


    


