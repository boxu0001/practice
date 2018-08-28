# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# Example:
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
class Solution:
    def maxSubArray(self, nums):
        si=0
        mx = nums[0]
        for i in nums[0:]:
            if si+i >= 0:
                si+=i
                if si > mx:
                    mx = si
            else:
                #if si < 0, it is a gap, newMax if exist, it must be from the next of the gap
                si=0
                if i > mx:
                    mx = i
        return mx

    def maxSub2(self, nums):
        max_sum = csum = nums[0]
        for num in nums[1:]:
            if num >= csum + num:
                csum = num
            else:
                csum += num
            
            if csum > max_sum:
                max_sum = csum        
        return max_sum

s=Solution()

print(s.maxSubArray([1,2]))
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(s.maxSubArray([-2,-1]))
print(s.maxSubArray([-1,1,2,1]))