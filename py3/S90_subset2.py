# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
# Note: The solution set must not contain duplicate subsets.

# Example:

# Input: [1,2,2]
# Output:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        stack=[-1]
        result=[[]]
        nums.sort()
        keys={}         #keys存每个元素的最后一个index
        for i, number in enumerate(nums):
            keys[number] = i
        ls=len(nums)
        nextChildIdx = 0
        while stack:
            if nextChildIdx >= ls:
                curIdx = stack.pop()                    #这里注意，如果stack最后仅剩-1，那么python的list[-1],指向最后一个元素
                nextChildIdx = keys[nums[curIdx]] + 1   #所以 keys[-1]+1 == ls, 意味这遍历结束，所以满足逻辑需要
            else:
                stack+=[nextChildIdx]
                result+=[[nums[x] for x in stack[1:]]]
                nextChildIdx+=1
        
        return result

s=Solution()
s.subsetsWithDup([1,2,2])