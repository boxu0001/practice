'''
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # recursion implementation
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        if root.left == None and root.right == None:
            return [root.val]
        else:
            result = [root.val]
            if root.left:
                result.extend(self.preorderTraversal(root.left))
            if root.right:
                result.extend(self.preorderTraversal(root.right))
            return result
            

    #stack based implementation
    def preorderTraversal2(self, root: TreeNode) -> List[int]:
        stack = [root] if root else []
        result = []
        while stack:
            node = stack.pop()
            result+=[node.val]
            if node.right:  #put right first
                stack.append(node.right)
            if node.left:   #then put left second
                stack.append(node.left)
        return result
                        