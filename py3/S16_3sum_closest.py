from __future__ import annotations
# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

# Example:
# Given array nums = [-1, 2, 1, -4], and target = 1.
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ls = len(nums)
        result = None
        for ai in range(0, ls-2):
            bi = ai+1
            ci = ls-1
            while bi < ci:
                currResult =  nums[ai] + nums[bi] + nums[ci]
                if currResult == target:
                    return target
                elif result == None:
                    result = currResult
                elif abs(target - currResult) < abs(target-result): #基本思路和3sum一致， 只有这里用abs取值比较
                    result = currResult
                else:
                    pass
                
                if currResult < target:
                    bi+=1
                else:
                    ci-=1

        return result

s=Solution()
print(s.threeSumClosest([-1, 2, 1, -4], -1))



    

