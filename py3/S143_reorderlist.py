'''
143. Reorder List
Medium

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.

Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        dummy = ListNode(-1)
        dummy.next = head
        tail = head
        midp = dummy
        
        while tail:
            tail = tail.next
            midp = midp.next  #if even, mid ends in smaller half, if odd, mid ends in mid
            if tail:
                tail = tail.next
        mid = midp.next
        #reverse from mid to end
        itr = mid
        itrx = itr.next if itr else None
        while itr and itrx:
            itrxnx = itrx.next
            itrx.next=itr
            itr = itrx
            itrx = itrxnx
        if midp:
            midp.next = None
        if mid:
            mid.next = None
        
        while head and itr:
            itrx = itr.next
            itr.next = head.next
            head.next = itr
            head = itr.next
            itr = itrx
            
    def reorderList2(self, head: ListNode) -> None:
        ln=0
        itr=head
        while itr:
            endPrev = itr
            while endPrev and endPrev.next and endPrev.next.next:
                endPrev = endPrev.next
            if endPrev != itr:
                end = endPrev.next
                endPrev.next = None
                end.next=itr.next
                itr.next=end
                itr = end.next
            else:
                return