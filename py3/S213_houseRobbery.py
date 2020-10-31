'''
213. House Robber II
Medium

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:

Input: nums = [0]
Output: 0

 

Constraints:

    1 <= nums.length <= 100
    0 <= nums[i] <= 1000
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        #f[i]=max(f[i-1], f[i-2]+nums[i]) for i < n-1
        #f[n-1]=max(f[n-2], f[n-3]+nums[i] if s[n-3] != 0)
        N=len(nums)
        f0=[None]*N     #以0为开头的计算， 
        f1=[None]*N     #以1为开头的计算
        f0[0]=nums[0]
        f1[0]=0
        
        for i in range(1, N):
            if i == 1:
                f0[i] = f0[0]
                f1[i] = nums[1]
            elif i < N-1:
                f0[i] = max(f0[i-2]+nums[i], f0[i-1])
                f1[i] = max(f1[i-2]+nums[i], f1[i-1])
            else:
                f0[i]=f0[i-1]                           #头尾不相连，所以不考虑 f0[i-2]
                f1[i] = max(f1[i-2]+nums[i], f1[i-1])   #f1 需要考虑

        
        return max(f0[-1], f1[-1])
    
        