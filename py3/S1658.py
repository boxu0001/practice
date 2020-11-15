'''
1658. Minimum Operations to Reduce X to Zero
Medium

You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it's possible, otherwise, return -1.

 

Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.

Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1

Example 3:

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.

 

Constraints:

    1 <= nums.length <= 105
    1 <= nums[i] <= 104
    1 <= x <= 109

'''

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        N=len(nums)
        lfsum = [0]
        for n in nums: lfsum += [n+lfsum[-1]]
        
        if lfsum[-1] < x:
            return -1
        
        rtsum = [0]
        for m in nums[::-1]: rtsum += [m+rtsum[-1]]

        res = -1
        i = 0
        j = N
        while i < j:
            if lfsum[i] + rtsum[j] == x:
                res = i+j if res == -1 else min(i+j, res)
            
            if lfsum[i] + rtsum[j] >= x:
                j-=1
            else:
                i+=1
            
        return res
            
        