# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

#     The left subtree of a node contains only nodes with keys less than the node's key.
#     The right subtree of a node contains only nodes with keys greater than the node's key.
#     Both the left and right subtrees must also be binary search trees.

# Example 1:

#     2
#    / \
#   1   3

# Input: [2,1,3]
# Output: true

# Example 2:

#     5
#    / \
#   1   4
#      / \
#     3   6

# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack=[root] if root else []
        
        goLeft = True
        lastPoped=None
        while stack:
            if stack[-1].left and goLeft:
                    stack+=[stack[-1].left]
            elif stack[-1].left == None and goLeft:
                goLeft = False
            else:
                curNode = stack.pop()
                if lastPoped and lastPoped.val >= curNode.val:  #pop之后做比较，看是否满足
                    return False
                lastPoped = curNode
        
                if curNode.right == None:
                    pass
                else:
                    stack+=[curNode.right]
                    goLeft = True
        return True                

#使用中序遍历， 
# 1. 使用一个goLeft变量，遍历左或者右，
# 2. 遍历左侧，push操作
# 3. 遍历右侧之前， pop当前节点，做中序遍历
# 4. 接着遍历右侧

