class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums)-1
        left=-1
        right=-1
        findSome = self.binSearch(nums, target, start, end)
        left = findSome
        right = findSome
        result1 = left
        result2 = right
        while left > -1:
            result1 = left
            left = bs(nums, target, start, left-1)
        
        while right > -1:
            result2 = right
            right = bs(nums, target, right+1, end)
        
        return [result1, result2]
        
        
    def binSearch(self, nums, target, start, end):
        si = start
        ei = end
        while si <= ei:
            mid = (si+ei)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                si = mid+1
            else:
                ei = mid-1
        return -1

#using binary search to search
#1. find left-most valid one if possible, or -1
#2. find right-most valid one if possible or -1
