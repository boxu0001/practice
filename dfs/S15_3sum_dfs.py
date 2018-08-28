# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
# Note:
# The solution set must not contain duplicate triplets.
# Example:
# Given array nums = [-1, 0, 1, 2, -1, -4],
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

#DFS version is slower than the other solutino, only demo DFS here
class Solution:
    def threeSum(self, nums):
        nums.sort()
        ne=0
        ls=len(nums)
        result=[]
        stack=[]
        sum=0
        while ls > ne >=0:
            stack+=[ne]
            sum+=nums[ne]
            if len(stack) < 3 and ne < ls-1:
                ne+=1
                continue 
            if len(stack) == 3 and sum == 0:
                result+=[[nums[i] for i in stack]]
            if sum >= 0:                
                sum-=nums[stack.pop()]               
            ne=ls
            while len(stack) > 0 and ne == ls:
                ti = stack.pop()
                sum-=nums[ti]
                ne = ti + 1
                while ne < ls and nums[ne] == nums[ti]:
                    ne += 1
        return result

s=Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))

    




