# 106. Construct Binary Tree from Inorder and Postorder Traversal
# Medium

# Given inorder and postorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.

# For example, given

# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]

# Return the following binary tree:

#     3
#    / \
#   9  20
#     /  \
#    15   7

# Definition for a binary tree node.

from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        elif len(inorder) == 1:
            return TreeNode(inorder[0])
        else:
            rt = postorder[-1] #root element
            root = TreeNode(rt) 
            idx = inorder.index(rt) 
            left = self.buildTree(inorder[:idx], postorder[:idx])
            right = self.buildTree(inorder[idx+1:], postorder[idx:-1])
            root.left = left
            root.right = right
            return root

class SolutionByStack:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        idx={}
        for (i,v) in enumerate(inorder):
            idx[v] = i
        
        if not postorder:
            return None
        root = TreeNode(postorder[-1])
        stack=[root]
        for v in postorder[-2::-1]:
            curNode = TreeNode(v)
            if idx[v] > idx[stack[-1].val]:
                stack[-1].right = curNode
                stack+=[curNode]
            else:
                poped = None
                while stack and idx[v] < idx[stack[-1].val]:
                    poped = stack.pop()
                if poped != None:
                    poped.left = curNode
                    stack+=[curNode]

        return root


s=SolutionByStack()
rrtt = s.buildTree([9,3,15,20,7],[9,15,7,20,3])
# rrtt = s.buildTree([9,3],[9,3])
rrtt2 = s.buildTree([3,2,1],[3,2,1])
