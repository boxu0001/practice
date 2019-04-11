from __future__ import annotations
# 107. Binary Tree Level Order Traversal II
# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

# For example:
# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7

# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = [root]
        nextQ = []
        while queue:
            top = queue.pop(0)
            if top.left != None:
                nextQ+=[top.left]
            if top.right != None:
                nextQ+=[top.right]
            if not queue:
                if nextQ:
                    result = [[i.val for i in nextQ]] + result
                queue = nextQ
                nextQ = [] 
        result+=[[root.val]] 
        return result

a=Solution()
r=TreeNode(9)
r.left=TreeNode(8)
r.right=TreeNode(7)
r.right.right=TreeNode(5)

print(a.levelOrderBottom(r))

        

            
		



