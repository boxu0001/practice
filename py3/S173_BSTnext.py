'''
173. Binary Search Tree Iterator
Medium

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

 

Example:

BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false

 

Note:

    next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
    You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        
        self.stack = [root] if root else []
        while self.stack and self.stack[-1].left:
            top = self.stack[-1]
            self.stack+=[top.left]
    
    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.stack:
            top =self.stack.pop()
            if top.right:
                self.stack+=[top.right]
                while self.stack[-1].left:
                    nxt = self.stack[-1]
                    self.stack+=[nxt.left]
            return top.val
        else:
            return None
        
#注意中序遍历的stack的压弹顺序，
#  压：top左边，直到没有; 
#  弹：top弹出，压top的右边节点，再做压：top左边，直到没有;