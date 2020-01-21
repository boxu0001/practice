'''
145. Binary Tree Postorder Traversal
Hard

Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        result=[]
        if root.left:
            result.extend(self.postorderTraversal(root.left))   #左子树
        if root.right:
            result.extend(self.postorderTraversal(root.right))  #右子树
        result+=[root.val]                                      #根
        return result
    
    def postorderTraversal2(self, root: TreeNode) -> List[int]:
        stack=[[root, 2]] if root else []
        result=[]
        while stack:
            cnode, bch = stack[-1]  #当前节点， 当前分支
            if bch == 2:
                if cnode.left:
                    stack+=[[cnode.left, 2]]
                else:
                    stack[-1][1]-=1
            elif bch == 1:
                if cnode.right:
                    stack+=[[cnode.right, 2]]
                else:
                    stack[-1][1]-=1
            else:
                stack.pop()
                result+=[cnode.val]
                if stack:
                    stack[-1][1]-=1
                
        return result