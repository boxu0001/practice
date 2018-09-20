'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

import cProfile, pstats,io

class Solution:
    #this is 2^n solution
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        max=1<<len(nums)
        for m in range(0, max):
            x=m
            xi=0
            t=[]
            while(x > 0) :
                if x & 1 == 1:
                    t.append(nums[xi])
                xi+=1
                x=x>>1
            result.append(t)
        return result

    #stack based DFS solution
    def subsetsDFS(self, nums):
        result=[]
        result.append([])
        ln=len(nums)
        stack=[]
        nei=0 if ln > 0 else None
        while(nei != None):
            if nei >= ln:
                stack.pop()
                nei = None if len(stack) == 0 else stack.pop() + 1
                continue
            stack.append(nei)
            result.append([nums[i] for i in stack])
            nei += 1
        return result
s=Solution()
cProfile.run("s.subsetsDFS(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', '0','1','2'])")
cProfile.run("s.subsets(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', '0','1','2'])")


