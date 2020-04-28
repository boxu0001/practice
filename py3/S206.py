'''
206. Reverse Linked List
Easy

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList1(self, head: ListNode) -> ListNode:
        return self.recursive(None, head)
        
    def recursive(self, cur, nxt):
        if nxt == None:
            return cur
        else:
            tmp = nxt.next
            nxt.next = cur
            return self.recursive(nxt, tmp)
    
    def reverseList(self, head: ListNode) -> ListNode:
        cur = None
        nxt = head
        while nxt:
            nxt.next, nxt, cur = cur, nxt.next, nxt
        return cur
