'''
124. Binary Tree Maximum Path Sum
Hard
Given a non-empty binary tree, find the maximum path sum.
For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:
Input: [1,2,3]

       1
      / \
     2   3

Output: 6

Example 2:
Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        curMax=None
        stack=[root] if root else []
        visited=[[]]
        while stack:
            curNode = stack[-1]
            curVisited = visited[-1]
            if len(curVisited) == 0:
                if curNode.left:
                    stack+=[curNode.left]
                    visited+=[[]]
                else:
                    visited[-1]+=[0]
            elif len(curVisited) == 1:
                if curNode.right:
                    stack+=[curNode.right]
                    visited+=[[]]
                else:
                    visited[-1]+=[0]
            else:
                stack.pop()
                visited.pop()
                leftChildMax = curVisited[0] if curVisited[0] > 0 else 0
                rightChildMax = curVisited[1] if curVisited[1] > 0 else 0
                tmpMax = curNode.val + leftChildMax + rightChildMax
                if curMax == None or curMax < tmpMax:
                    curMax = tmpMax
                if visited:
                    visited[-1] += [max(leftChildMax, rightChildMax) + curNode.val]
        return curMax
                        