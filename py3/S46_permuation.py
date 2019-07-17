# Given a collection of distinct integers, return all possible permutations.
# Example:
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
from __future__ import annotations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        ls=len(nums)
        visited=[False]*ls
        stack=[-1]
        nxtChildIdx=0
        while len(stack) > 0:
            if nxtChildIdx < ls and visited[nxtChildIdx]:
                nxtChildIdx += 1
            elif nxtChildIdx < ls:
                stack+=[nxtChildIdx]
                visited[nxtChildIdx]=True    
                nxtChildIdx=0
                if len(stack) == ls+1:
                    result+=[[nums[i] for i in stack[1:]]]
            else:
                childIdx=stack.pop()
                if childIdx >= 0:
                    visited[childIdx]=False
                    nxtChildIdx=childIdx+1
        return result

    def permute2(self, nums: List[int]) -> List[List[int]]:
        result = []
        ls = len(nums)
        if ls == 0:
            return result
        elif ls == 1:
            result += [nums]
        else:
            for i in range(ls):
                subnums=nums[:i]+nums[i+1:]
                subresult=self.permute2(subnums)
                for j in subresult:
                    result+=[[nums[i]] + j]
        return  result

s=Solution()
r=s.permute2([1,2,3])
print(r)