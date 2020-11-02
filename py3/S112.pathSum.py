'''
112. Path Sum
Easy

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1

return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        #preorder
        stack=[[root, 1]] if root else []  #1 go left, 0 go right, -1 done
        if root:
            sum-=root.val
        while stack:
            node, d = stack[-1]
            if node.left == None and node.right == None and sum == 0:
                return True
            
            if d < 0:
                stack.pop()
                sum+=node.val
            elif d == 1 and node.left:
                stack[-1][1]-=1    
                stack+=[[node.left, 1]]
                sum-=node.left.val
            elif d == 0 and node.right:
                stack[-1][1]-=1
                stack+=[[node.right, 1]]
                sum-=node.right.val
            else:
                stack[-1][1]-=1
            
        return False
                
    def hasPathSum2(self, root, sum):
        if root is None:
            return False
        if root.left is None and root.right is None:
            return sum == root.val 
        else:
            return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)    

