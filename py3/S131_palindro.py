from __future__ import annotations

# Given a string s, partition s such that every substring of the partition is a palindrome.

# Return all possible palindrome partitioning of s.

# Example:

# Input: "aab"
# Output:
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]



class Solution:
    def partition(self, s: str) -> List[List[str]]:
        sl = len(s)

        f=[[] for i in range(sl)]
        
        #find all palindrome by s[i:j]
        for i in range(sl):
            for j in range(i+1, sl+1):
                if s[i:j] == s[i:j][::-1]:
                    f[i]+=[j]

        #then use DFS to go deep on the tree
        result=[]
        stack=[[0,0]] if sl > 0 else []     #each entry on stack is [i, ii] and j=f[i][ii]， i是字符串的index, ii是f[i]数组的index
        while stack:
            [i, ii] = stack[-1]
            if ii < len(f[i]):
                j = f[i][ii]
                if j == sl:     #访问到最后位置 加入result
                    result+=[[s[xi:f[xi][xii]] for xi, xii in stack]]
                    stack.pop()
                    if stack:
                        stack[-1][1]+=1     #这里是 ii++
                else:                       
                    stack+=[[j, 0]]         #下一个上栈
            else:
                stack.pop()                 
                if stack:
                    stack[-1][1]+=1
        return result
 

s=Solution()
s.partition('aab')