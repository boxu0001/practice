'''
222. Count Complete Tree Nodes
Medium

Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    #using binary search
    def countNodes(self, root: TreeNode) -> int:
        h=0
        itr=root
        while itr:
            h+=1
            itr=itr.left
        
        left=1<<(h-1)
        right=(1<<h) - 1

        if self.numberReachable(root, right, h):
            return right

        while left < right:
            mid = (left+right)//2
            if self.numberReachable(root, mid, h):
                left = mid+1
            else:
                right=mid
        
        if self.numberReachable(root, left, h):
            return left
        else:
            return left-1

    def numberReachable(self, root, num, h):
        reachable=True
        itr = root
        for i in range(h-1, 0, -1):
            if itr == None:
                break
            lr = num>>(i-1) & 1 # eg. path 100 -> root -> left -> left; 110: root->right->left
            if lr == 0:
                itr = itr.left
            else:
                itr = itr.right
        if itr == None:
            reachable = False

        return reachable

    # BFS counting
    def countNodes2(self, root: TreeNode) -> int:
        count=0
        queue=[root] if root else []
        while queue:
            tmp=[]
            nd= queue.pop()
            count+=1
            if nd.left:
                queue+=[nd.left]
            if nd.right:
                queue+=[nd.right]
            
        return count
            

s=Solution()

n=TreeNode(1)
n.left=TreeNode(2)
n.right=TreeNode(3)
n.left.left=TreeNode(4)
n.left.right=TreeNode(5)
n.right.left=TreeNode(6)

s.countNodes(n)