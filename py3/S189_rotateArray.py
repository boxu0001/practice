'''
189. Rotate Array
Easy

Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
'''

from __future__ import annotations
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        start=0
        ls = len(nums)
        k=k%ls
        done=[False for _ in range(k)]
        for i in range(k):
            curval = nums[i]
            nxtval = None
            while not (i<k and done[i]):
                nxti = (i+k)%ls
                nxtval = nums[nxti]
                nums[nxti] = curval
                curval = nxtval
                if 0<= i < k:
                    done[i] = True
                i = nxti
        return

    def rotate2(self, nums: List[int], k: int) -> None:
        ls=len(nums)
        k=k%ls
        nums[:k], nums[k:] = nums[ls-k:], nums[0:ls-k]
        return
                
s=Solution()
s.rotate([1,2,3,4,5,6,7], 3)