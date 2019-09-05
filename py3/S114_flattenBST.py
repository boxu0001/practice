'''
114. Flatten Binary Tree to Linked List
Medium

Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6

The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:            
        stack=[root] if root else []
        visited=[2]
        poped=None
        while stack:
            curNode = stack[-1]
            if visited[-1] == 2 and curNode.right:  # 2 为访问右子树
                stack+=[curNode.right]
                visited+=[2]
            elif visited[-1] == 1 and curNode.left: # 1 为访问左子树
                stack+=[curNode.left]
                visited+=[2]
            elif visited[-1] == 0:                  # 0 左右子数都访问完了
                lastPoped = poped
                poped=stack.pop()
                visited.pop()
                poped.left = None
                poped.right = lastPoped
                if visited:                         
                    visited[-1]-=1                  #pop完要更新父节点的访问状态
            else:
                visited[-1]-=1                      #如果left or right 为 None, 要更新父节点的访问状态

#使用了反向的后序遍历， 右树 -> 左树 -> 中间节点
#注意， 中序(左中右)遍历和后序(左右中)遍历都需要 stack, 先序(中左右)用queue

'''
# 中序(左中右) 的遍历， 注意只用一个变量控制遍历方向， goLeft
        stack=[root] if root else []
        goLeft = True
        while stack:
            if stack[-1].left and goLeft:
                stack+=[stack[-1].left]
            elif stack[-1].left == None and goLeft:
                goLeft = False
            else:
                curNode = stack.pop()
                if curNode.right != None:
                    stack+=[curNode.right]
                    goLeft = True
        return True                
'''