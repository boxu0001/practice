'''
673. Number of Longest Increasing Subsequence
Medium

Given an integer array nums, return the number of longest increasing subsequences.

 

Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].

Example 2:

Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.

 

Constraints:

    0 <= nums.length <= 2000
    -106 <= nums[i] <= 106

'''
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        #f[i] i is end, number of longest,  0<=k<=i, max(f[k])+1
        #c[i] i is end, count of length, count(f[k]==max)
        N=len(nums)
        f=[1]*N if N > 0 else []
        c=[1]*N if N > 0 else []
        maxLen = 1
        for i in range(1, N):
            for k in range(i):
                if nums[i] > nums[k]:
                    if f[k]+1>f[i]:
                        f[i] = f[k]+1
                        c[i] = c[k]
                    elif f[k]+1==f[i]:
                        c[i] += c[k]
                
            if f[i] > maxLen:
                maxLen = f[i]
        
        count=sum([c[k] for k in range(N) if f[k] == maxLen])
        
        return count
        
