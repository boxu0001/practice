'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''

class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k==0 or n==0:
            return [[]]
        result=[]
        stack=[]
        nextEle=1
        while(True):
            l=len(stack)
            if nextEle + k - l - 1 > n and l > 0 :
                nextEle = stack.pop() + 1
            elif nextEle + k - l - 1 <= n:
                stack+=[nextEle]
                if l == k-1:
                    result.append(stack[:])
                    nextEle=stack.pop()+1
                else:
                    nextEle=stack[-1]+1
            else:
                return result

s=Solution()
print(s.combine(4,2))
print(s.combine(0,1))




