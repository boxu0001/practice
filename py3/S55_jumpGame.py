# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Determine if you are able to reach the last index.

# Example 1:

# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:

# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
#              jump length is 0, which makes it impossible to reach the last index.


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curmax=nums[0]
        ls=len(nums)
        for i, di in enumerate(nums):
            if i <= curmax:
                curmax=max(curmax, i+di)    #i+di 为当前位置能到达最大位置
                if curmax >= ls-1:          # 让它和curmax比较
                    return True
            else:                           #如果当前位置都无法到达，那么也无法到达最后位置
                return False
        return True
        