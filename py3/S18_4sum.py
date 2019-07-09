from __future__ import annotations
# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

# Note:

# The solution set must not contain duplicate quadruplets.

# Example:
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ls = len(nums)
        result=[]
        for ai in range(ls-3):
            if nums[ai]*4 <=target and (ai == 0 or nums[ai] != nums[ai-1]):
                for bi in range(ai+1, ls-2):
                    if nums[ai]+3*nums[bi] <= target and (bi==ai+1 or nums[bi]!=nums[bi-1]):
                        ci=bi+1
                        di=ls-1
                        while ci < di:
                            if ci > bi+1 and nums[ci] == nums[ci-1]:
                                ci+=1
                                continue
                            if di < ls-1 and nums[di] == nums[di+1]:
                                di-=1
                                continue
                            if nums[ai]+nums[bi]+nums[ci]+nums[di] == target:
                                result += [[nums[ai], nums[bi], nums[ci], nums[di]]]
                                ci+=1
                                di-=1
                            elif nums[ai]+nums[bi]+nums[ci]+nums[di] < target:
                                ci+=1
                            else:
                                di-=1
        return result 


    def fourSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ls = len(nums)
        result=[]
        sum2Cache={}
        for yi in range(ls-1, 2, -1):
            if yi==ls-1 or nums[yi] != nums[yi+1]:
                for xi in range(yi-1, 1, -1):
                    if xi==yi-1 or nums[xi] != nums[xi+1]:    
                        t2=nums[xi]+nums[yi]
                        if t2 not in sum2Cache:
                            sum2Cache[t2]=[]
                        sum2Cache[t2]+=[[xi,yi]]
        
        for ai in range(ls-3):
            if nums[ai]*4 <=target and (ai == 0 or nums[ai] != nums[ai-1]):
                for bi in range(ai+1, ls-2):
                    if nums[ai]+3*nums[bi] <= target and (bi==ai+1 or nums[bi]!=nums[bi-1]):
                        t2 = target-nums[ai]-nums[bi]
                        if t2 in sum2Cache:
                            for ci, di in sum2Cache[t2]:
                                if ci > bi:
                                    result+=[[nums[ai], nums[bi], nums[ci], nums[di]]]

        return result 


s=Solution()
print(s.fourSum2([-1,2,2,-5,0,-1,4],3))