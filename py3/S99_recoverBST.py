"""
99. Recover Binary Search Tree
Hard

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2

Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3

Follow up:

    A solution using O(n) space is pretty straight forward.
    Could you devise a constant space solution?

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        #inorder traversal
        stack=[root] if root else []
        firstBig=None
        lastSmall=None
        goLeft=True
        prevNode=None
        curNode=None
        while stack:
            if goLeft and stack[-1].left:
                stack+=[stack[-1].left]
            else:
                poped = stack.pop()
                if poped.right:
                    stack+=[poped.right]
                    goLeft=True
                else:
                    goLeft=False            #这之前都是inorder traversal的通用代码
                prevNode=curNode
                curNode=poped
                if prevNode and prevNode.val > curNode.val:
                    if firstBig==None:
                        firstBig=prevNode
                    lastSmall=curNode
        tmp=lastSmall.val
        lastSmall.val=firstBig.val
        firstBig.val=tmp
        
#使用inorder traversa
#变量 firstBig 存第一次出现的过大节点 a[k-1] < a[k] > a[k+1]...中的a[k] 
#变量 lastSmall 存最后出现的过小节点 ...< a[t-1] > a[t] < a[t+1]...中的a[t] 
#最后做 firstBig lastSmall 数值交换
                