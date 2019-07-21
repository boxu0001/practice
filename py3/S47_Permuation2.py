# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
# Example:
# Input: [1,1,2]
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]

class Solution:
    #此解法未作技术总结，请参考下面的解法
    def permuteUnique(self, sublist):
        lsb = len(sublist)
        if lsb <= 1:
            return [sublist if lsb==1 else []]
        else:
            result = []
            p0list = self.permuteUnique(sublist[1:])
            for e in p0list:
                    result += [[sublist[0]] + e]
            i=1
            swapped={sublist[0]}
            while(i<lsb):
                if sublist[i] not in swapped :
                    #swap and recursiveP
                    anewlist=sublist[1:]
                    anewlist[i-1] = sublist[0]
                    plist = self.permuteUnique(anewlist)
                    for e in plist:
                        result += [[sublist[i]] + e]
                    swapped.add(sublist[i])
                i+=1
            return result   

#对树结构的深度遍历，通常两种算法，异曲同工
#第一种用recursion,递归调用
#第二种用stack, 进行DFS遍历

    #第一种 DFS
    def permuteUniqueDFS(self, nums):
        nums.sort()
        ls=len(nums)
        stack=[-1]              #注意，用一个dummy node作为root 节点
        nxtNode=0
        visited=[False]*ls      #注意，用一个list来存储当前访问过的状态， visited[i] = True/False, 表明访问过没有
        result=[]
        while stack:            #接下来就是判断树的遍历条件：探索 VS 回滚
            curNode=stack[-1]  
            if ls > nxtNode >= 0:       #如果子节点存在，接续探索
                stack+=[nxtNode]
                visited[nxtNode] = True
                if len(stack) == ls+1:
                    result+=[[nums[i] for i in stack[1:]]]
                #find next child node,
                nxtNode=ls
                for i in range(ls):
                    if not visited[i]:  #找到下一个未访问的节点
                        nxtNode=i
                        break
            else:                       #如果子节点全部遍历完了，回滚
                #rollback   
                poped = stack.pop()
                if poped < 0:
                    continue
                visited[poped] = False
                nxtNode=ls
                for i in range(poped+1, ls):
                    if not visited[i] and nums[i] != nums[poped]:   #注意，这里下个节点要满足未访问并且不能与pop的重复
                        nxtNode=i
                        break
        return result

    #第二种recursion
    def permuteUniqueRecursion(self, nums):
        nums.sort()
        return self.permuteUniqueRec(nums)
                
    def permuteUniqueRec(self, nums: List[int]) -> List[List[int]]:
        r=[]
        ls=len(nums)
        if ls==0:
            return r
        elif ls==1:
            return [nums]
        else:
            lasti=None
            for i in range(ls):
                if lasti == None or nums[lasti] != nums[i]:
                    rchildren=self.permuteUniqueRec(nums[:i] + nums[i+1:])
                    for ri in rchildren:
                        r+=[[nums[i]] + ri]
                lasti = i
            return r
        





s = Solution()
print(s.permuteUniqueRecursion([1,2,2,3,3]))
