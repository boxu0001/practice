'''
Given a binary tree, find the subtree with maximum average. Return the root of the subtree.

LintCode will print the subtree which root is your return node.
It's guaranteed that there is only one subtree with maximum average.
Have you met this question in a real interview?  
Example

Example 1

Input：
{1,-5,11,1,2,4,-2}
Output：11
Explanation:
The tree is look like this:
     1
   /   \
 -5     11
 / \   /  \
1   2 4    -2 
The average of subtree of 11 is 4.3333, is the maximun.

Example 2

Input：
{1,-5,11}
Output：11
Explanation:
     1
   /   \
 -5     11
The average of subtree of 1,-5,11 is 2.333,-5,11. So the subtree of 11 is the maximun.
'''


"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    def findSubtree2(self, root):
        # write your code here
        _, _, _, nd  = self.findSubtreeRecursive(root)
        return nd
    
    
    def findSubtreeRecursive(self, node):
        if node == None:
            return [0, 0, None, None]
        if node.left == None and node.right==None:
            return [1, node.val, node.val, node]
        else:
            cnt=1
            smt=node.val
            lfmxavg = None
            rtmxavg = None
            if node.left:
                lfcnt, lfsum, lfmxavg, lftnode = self.findSubtreeRecursive(node.left)
                cnt+=lfcnt
                smt+=lfsum
                    
                    
            if node.right:
                rtcnt, rtsum, rtmxavg, rtnode = self.findSubtreeRecursive(node.right)
                cnt+=rtcnt
                smt+=rtsum
            
            mxavg = smt/cnt
            mxnode = node
            
            if lfmxavg and lfmxavg > mxavg:
                mxavg = lfmxavg
                mxnode = lftnode
                
            if rtmxavg and rtmxavg > mxavg:
                mxavg =rtmxavg
                mxnode= rtnode
            
            return [cnt, smt, mxavg, mxnode]


s=Solution()
{1,-5,11,1,2,4,-2}
n=TreeNode(1)
n.left=TreeNode(-5)
n.right=TreeNode(11)
n.left.left=TreeNode(1)
n.left.right=TreeNode(2)
n.right.left=TreeNode(4)
n.right.right=TreeNode(-2)


s.findSubtree2(n)