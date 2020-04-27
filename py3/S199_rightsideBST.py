'''
199. Binary Tree Right Side View
Medium

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        result=[]
        curlevel=[root] if root else []
        while curlevel:
            result+=[curlevel[0].val]
            nxtlevel=[]
            for e in curlevel:
                if e.right:
                    nxtlevel+=[e.right]
                if e.left:
                    nxtlevel+=[e.left]
            curlevel=nxtlevel
        
        return result
            
            
            
            