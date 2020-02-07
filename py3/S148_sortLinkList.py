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

    #using Quick Sort      
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

    #using merge sort, using slow, fast iterators
    def mergeSort(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        elif head.next.next == None:
            if head.next.val < head.val:
                b=head.next
                b.next = head
                head.next = None
                return b
            else:
                return head
        else:
            mid=head
            tail=head
            while tail.next != None and tail.next.next != None:
                tail = tail.next.next
                mid = mid.next
            secondHead = mid.next
            mid.next = None
            firstHalf = self.mergeSort(head)
            secondHalf = self.mergeSort(secondHead)
            dummy = ListNode(0)
            itr = dummy
            while firstHalf != None or secondHalf != None:
                if secondHalf == None or (firstHalf != None and firstHalf.val < secondHalf.val):
                    itr.next = firstHalf
                    firstHalf = firstHalf.next
                else:
                    itr.next = secondHalf
                    secondHalf = secondHalf.next
                itr = itr.next
            return dummy.next

    #merge sort using stack version
    def mergeSortStack(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        stack=[[dummy, None]] if head else []

        #push split on stack
        while stack:
            firstHalf, secondHalf = stack[-1]
            if firstHalf.next != None and secondHalf == None:
                # split
                mid = firstHalf.next
                tail = firstHalf.next
                while tail.next != None and tail.next.next != None:
                    tail = tail.next.next
                    mid = mid.next
                if mid.next != None:
                    secondHalf = ListNode(0)
                    secondHalf.next = mid.next
                    mid.next = None
                    stack[-1][1] = secondHalf
                    # push new half on stack
                    stack+=[[firstHalf, None], [secondHalf, None]]
                else:
                    # if mid.next == None, firstHalf.next is a single Node list, simplely pop
                    stack.pop()
            else:
                # merge
                itr = firstHalf
                A = firstHalf.next
                B = secondHalf.next
                while A != None or B != None:
                    if B == None or (A != None and A.val < B.val):
                        itr.next = A
                        A = A.next
                    else:
                        itr.next = B
                        B = B.next
                    itr = itr.next
                stack.pop()

        return dummy.next





head = ListNode(4)
head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(1)
# head.next.next.next.next = ListNode(5)

s=Solution()
t=s.mergeSortStack(head)
