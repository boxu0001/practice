# 148. Sort List
# Medium

# Sort a linked list in O(n log n) time using constant space complexity.

# Example 1:

# Input: 4->2->1->3
# Output: 1->2->3->4

# Example 2:

# Input: -1->5->3->4->0
# Output: -1->0->3->4->5



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        newHead, _ = self.innerSort(head)
        return newHead
    
    def innerSort(self, head:ListNode):
        pivot = head
        if head.next == None:
            return head, head
        
        lsmall = None
        llarge = None
        itr = head.next if head else None
        while itr:
            if llarge == None and itr.val < pivot.val:
                lsmall = itr
                itr = itr.next
            elif itr.val >= pivot.val:
                llarge = itr
                itr = itr.next
            else: #llarge != None and itr.val < pivot.val:
                if lsmall == None:
                    lsmall = pivot
                newLLarge = lsmall.next
                newLSmall = itr
                itr = itr.next
                newLSmall.next = newLLarge.next if newLLarge.next != newLSmall else newLLarge
                newLLarge.next = itr
                lsmall.next = newLSmall
                llarge.next = newLLarge
                lsmall = newLSmall
                llarge = newLLarge
                
        fsmall = head.next if lsmall else None
        flarge = None
        if llarge:
            flarge = lsmall.next if lsmall else head.next
            llarge.next = None
        if lsmall:
            lsmall.next = None
        head.next = None
        
        if fsmall == None and flarge == None:
            return head, head
        elif fsmall == None and flarge != None:
            newLargeHead, newLargeTail = self.innerSort(flarge)
            head.next = newLargeHead
            return head, newLargeTail
        elif fsmall != None and flarge == None:
            newSmallHead, newSmallTail = self.innerSort(fsmall)
            newSmallTail.next = head
            return newSmallHead, head
        else:
            newSmallHead, newSmallTail = self.innerSort(fsmall)
            newLargeHead, newLargeTail = self.innerSort(flarge)
            newSmallTail.next = head
            head.next = newLargeHead
            return newSmallHead, newLargeTail


    def sortList2(self, head: ListNode) -> ListNode:
        itr = head
        l = []
        while itr:
            l.append(itr)
            itr = itr.next
        l.sort(key=lambda e: e.val)
        for i, ei in enumerate(l):
            ei.next = l[i+1] if i < len(l) -1 else None
        return l[0] if l else None

head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(1)

s=Solution()
s.sortList2(head)