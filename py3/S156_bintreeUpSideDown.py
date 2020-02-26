'''
Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.
Example

Example1

Input: {1,2,3,4,5}
Output: {4,5,2,#,#,3,1}
Explanation:
The input is
    1
   / \
  2   3
 / \
4   5
and the output is
   4
  / \
 5   2
    / \
   3   1

Example2

Input: {1,2,3,4}
Output: {4,#,2,3,1}
Explanation:
The input is
    1
   / \
  2   3
 /
4
and the output is
   4
    \
     2
    / \
   3   1
'''


#Definition of TreeNode:

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: the root of binary tree
    @return: new root
    """
    def upsideDownBinaryTree(self, root):
        # write your code here
        p, c, pr = None, root, None #parent, current, parent.right， 把根节点的虚拟parent和右邻节点设为None, 方便遍历
        while c:
            cl, cr = c.left, c.right    #注意节点的置换
            c.left, c.right = pr, p
            p, c, pr = c, cl, cr
            
            # p, c, pr, p.left, p.right = c, c.left,c.right, pr, p    # 这是简化版，注意tuple的分配，p.left, p.right， 因为c已经改变
        return p


r = TreeNode(1)
r.left = TreeNode(2)
r.right = TreeNode(3)
r.left.left = TreeNode(4)
r.left.right = TreeNode(5)
s=Solution()
s.upsideDownBinaryTree(r)