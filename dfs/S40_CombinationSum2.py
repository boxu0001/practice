# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
# Each number in candidates may only be used once in the combination.
# Note:
#     All numbers (including target) will be positive integers.
#     The solution set must not contain duplicate combinations.
# Example 1:
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]

# Example 2:
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
#   [1,2,2],
#   [5]
# ]

class Solution:
    def combinationSum2(self, candidates, target):
        result=[]
        ls = len(candidates)
        candidates.sort()    
        ne=0
        stack=[]
        rem=target
        while ls > ne >= 0:
            stack+=[ne]
            rem-=candidates[ne]
            if rem == 0: result+=[[candidates[i] for i in stack]]
            if rem > 0:
                ne+=1
            if (ne == ls and len(stack) > 0) or rem <= 0:
                rem+=candidates[stack.pop()]
                ne=ls
                while len(stack) > 0 and ne==ls:
                    ti=stack.pop()
                    rem+=candidates[ti]
                    ne=ti+1
                    while ne < ls and candidates[ne]==candidates[ti]:
                        ne+=1
        return result

s=Solution()        
print(s.combinationSum2([3,1,3,5,1,1], 8))
print(s.combinationSum2([1,2,3,4,5,6,7,8,9], 15))
