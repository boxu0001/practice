# Given a linked list, remove the n-th node from the end of list and return its head.

# Example:

# Given linked list: 1->2->3->4->5, and n = 2.

# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
# Given n will always be valid.
# Follow up:
# Could you do this in one pass?

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    #遍历两遍的解法，第一遍数个数，第二遍找位置，
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ls = 0
        curNode=head
        while curNode != None:
            ls+=1
            curNode = curNode.next
        i=0
        curNode=None
        while i < ls - n:
            curNode = head if curNode == None else curNode.next
            i+=1
            
        if curNode:
            rm = curNode.next
            curNode.next=rm.next
            rm.next=None    
        else:               #这里要注意头指针的删除情况
            rm = head
            head=rm.next
            rm.next=None
            
        return head
        
    #这是遍历一遍的解法，用双指针
    def removeNthFromEndOnePass(self, head: ListNode, n: int) -> ListNode:
        count=0
        dummyHead = ListNode(-1)
        dummyHead.next = head
        start=dummyHead
        end=dummyHead
        while end != None:
            if count <= n:      # from 0 to n, total n+1 
                count+=1
            else:
                start=start.next
            end=end.next
        rm = start.next
        if rm == head:
            head = rm.next
        start.next = rm.next
        rm.next = None
        return head
        




