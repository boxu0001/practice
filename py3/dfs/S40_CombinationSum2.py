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


        # c = [1,1,2,2,5,5]
        #       root
        #    /    |     \
        #   1     2      5
        #  /|\    |\      \
        # 1 2 5   2 5      5
    def dfsTree(self, c, t):
        result=[]
        c.sort()
        ls=len(c)
        # 1.define the stack
        stack=[-1]
        sumi=0
        # 2.define ni as next valid index
        ni=stack[-1]+1
        while stack:
            if ni >= ls or sumi+c[ni] >= t:     # 3a. rollback, 如果索引溢出或者求和超过或等于 （注意，这里有等于条件， 属于回滚条件）
                if ni < ls and sumi+c[ni] == t:     # 4a. 如果满足条件， 加入返回列中
                    #find one
                    ri=[c[i] for i in stack[1:]]
                    ri+=[c[ni]]
                    result+=[ri]
                pi = stack.pop()                    # 对于3a, 回滚， 抛出顶层元素
                ni=pi+1     #try next child node        #然后尝试下个元素
                if pi >= 0:                             #这里， pi可能是-1, 这样的话说明已经遍历完了，没有必要继续
                    sumi-=c[pi]                         #如果 pi>=0, 回滚和的值
                    while ni < ls and c[ni] == c[pi]:   #循环，这里的条件是 如果是抛出的元素相同的值（说明已经在这个结点已经遍历过）， 忽略并继续寻找
                        ni+=1   #until find one         #直到找到， 或者溢出， 溢出最终会被 3a 抓获
            else:                               #3b. 把下一个可探索的元素放入栈中
                stack+=[ni]
                sumi+=c[ni]
                #find next
                ni+=1                           #简单ni++
        return result
                
s=Solution()        
print(s.combinationSum2([3,1,3,5,1,1], 8))
print(s.dfsTree([3,1,3,5,1,1], 8))
print(s.combinationSum2([1,2,3,4,5,6,7,8,9], 15))
print(s.dfsTree([1,2,3,4,5,6,7,8,9], 15))