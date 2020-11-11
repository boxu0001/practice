'''
698. Partition to K Equal Sum Subsets
Medium

Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

 

Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

 

Note:

    1 <= k <= len(nums) <= 16.
    0 < nums[i] < 10000.
'''
from __future__ import annotations
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        N=len(nums)
        S=sum(nums)
        if S%k != 0:
            return False
        sg = S//k
        nums=sorted(nums)
        if nums[-1] > sg:
            return False
        groups = self.findGroups(nums, sg)
        if len(groups) == 0:
            return False

        numIdx={}
        for i, n in enumerate(nums):
            if n not in numIdx:
                numIdx[n]=[]
            numIdx[n]+=[i]

        FULL = (1<<N)-1

        kstack=[[0, 0]]
        while kstack:
            prvmask, nxtgi = kstack[-1]
            if prvmask == FULL and len(kstack)-1==k:
                return True

            if nxtgi < len(groups):
                nxtMask = prvmask
                givalid = True
                for n in groups[nxtgi]:
                    niValid = False
                    for ni in numIdx[n]:
                        if nxtMask & (1<<ni) == 0:
                            nxtMask |= (1<<ni)
                            niValid=True
                            break
                    if not niValid:
                        givalid = False
                        break
                if givalid:
                    kstack+=[[nxtMask, nxtgi]]
                else:
                    kstack[-1][1]+=1
            else:
                kstack.pop()
                if kstack:
                    kstack[-1][1]+=1

        return False
        
    def findGroups(self, nums, sg):
        N = len(nums)
        stack=[[-1, 0]]
        target = 0
        result=[]
        while stack:
            lsti, nxti = stack[-1]
            if nxti < N and target + nums[nxti] <= sg:
                stack+=[[nxti, nxti+1]]
                target += nums[nxti]
            else:
                if target == sg:
                    result+=[[nums[lsti] for lsti, _ in stack[1:]]]
                
                stack.pop()
                target -= nums[lsti]

                if stack:
                    li, oi = stack[-1]
                    nxti = oi+1
                    while (nxti < N and nums[nxti] == nums[oi]):
                        nxti+=1
                    stack[-1][1] = nxti

        return result

    #dfs
    def canPartitionKSubsets2(self, nums: List[int], k: int) -> bool:
        target, rem = divmod(sum(nums), k)
        if rem: return False

        def search(groups):
            if not nums: return True
            v = nums.pop()
            for i, group in enumerate(groups):
                if group + v <= target:
                    groups[i] += v
                    if search(groups): return True
                    groups[i] -= v
                if not group: break
            nums.append(v)
            return False

        nums.sort()
        if nums[-1] > target: return False
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1

        res = search([0] * k)

        return res

s=Solution()
s.canPartitionKSubsets2([5,4,3,3,2,2,1], 4)
