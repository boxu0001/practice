'''
337. House Robber III
Medium

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:

Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
'''
from __future__ import annotations
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: TreeNode) -> int:
        # f(node)  = max of f(left as root) + f(right as root)
        #               of f(left without left)  + f(right without right) + node
        #               of f(left without left) + f(right)
        #               of f(left) + f(right without right as root)
        # post order traversal
        stack=[[root, root.val, 0, 1]] if root else []
        res = 0
        while stack:
            node, rob, notrob, direction = stack[-1]
            if direction < 0:
                #pop
                stack.pop()
                res = max(res, rob, notrob)
                
                if stack:
                    stack[-1][1]+=notrob    #rob parent node, then this node should not be robbed
                    stack[-1][2]+=max(rob, notrob) # not rob parent, then find max of rob or notrob of current node
                    
            elif direction == 1:
                #push left
                stack[-1][-1]-=1
                if node.left:
                    stack+=[[node.left, node.left.val, 0, 1]]
                
            else:
                #push right
                stack[-1][-1]-=1
                if node.right:
                    stack+=[[node.right, node.right.val, 0, 1]]
                
        return res

    #using dfs
    def rob(self, root: TreeNode) -> int:
        def call(node):
            if not node:
                return (0,0)
            left = call(node.left)
            right = call(node.right)
            
            rob = node.val + left[1] + right[1]
            not_rob = max(left) + max(right)
            
            return (rob, not_rob)
        return max(call(root))