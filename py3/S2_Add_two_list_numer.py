# 2. Add Two Numbers
# Medium

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 算法属于简单的链表遍历， 注意 加法进位，以及头节点的返回
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = None   #头节点的返回
        overFlag = 0    #加法进位
        prevNode = None
        while l1 or l2 or overFlag != 0:    #判断基于任何一个都有值的情况
            l1v = l1.val if l1 else 0
            l2v = l2.val if l2 else 0
            currNode = ListNode((l1v+l2v+overFlag)%10)
            overFlag = (l1v+l2v+overFlag)//10
            if not result:
                result = currNode
                prevNode = result
            else:
                prevNode.next = currNode
                prevNode = prevNode.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return result

s=Solution()
a=ListNode(9)
a.next=ListNode(9)
a.next.next=ListNode(9)
b=ListNode(1)
r=s.addTwoNumbers(a,b)
while r:
    print(r.val)
    r=r.next
