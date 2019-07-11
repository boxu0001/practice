from __future__ import annotations
# 23. Merge k Sorted Lists
# Hard
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Example:
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    priorityQ=[]
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummyHead = ListNode(-1)
        curHead = dummyHead
        for li in lists:
            if li: self.addEndAndShiftUp(li)
        
        while len(self.priorityQ) > 0:
            nextNode = self.removeTopAndShiftDown()
            curHead.next = nextNode
            if nextNode.next:
                self.addEndAndShiftUp(nextNode.next)
            curHead = curHead.next

        return dummyHead.next

    def addEndAndShiftUp(self, node):
        self.priorityQ += [node]
        idx = len(self.priorityQ) - 1
        parentIdx = (idx-1)//2
        while parentIdx >=0 and self.priorityQ[idx].val < self.priorityQ[parentIdx].val:
            curNode = self.priorityQ[idx]
            self.priorityQ[idx] = self.priorityQ[parentIdx]
            self.priorityQ[parentIdx] = curNode
            idx = parentIdx
            parentIdx = (idx-1)//2
        return
    
    def removeTopAndShiftDown(self):
        top = self.priorityQ[0]
        if len(self.priorityQ) == 1:
            self.priorityQ.pop()
            return top
        self.priorityQ[0] = self.priorityQ.pop()
        ls = len(self.priorityQ)
        idx=0
        ch1idx = idx*2+1
        ch2idx = idx*2+2
        while (ch2idx < ls and self.priorityQ[ch2idx].val < self.priorityQ[idx].val) or (ch1idx < ls and self.priorityQ[ch1idx].val < self.priorityQ[idx].val):
            switchingChild = ch2idx if ch2idx < ls and self.priorityQ[ch2idx].val < self.priorityQ[ch1idx].val else ch1idx
            curNode = self.priorityQ[idx]
            self.priorityQ[idx] = self.priorityQ[switchingChild]
            self.priorityQ[switchingChild] = curNode
            idx = switchingChild
            ch1idx = idx*2+1
            ch2idx = idx*2+2
        return top

s=Solution()
nlist=[]
n1=ListNode(1)
n1.next=ListNode(4)
n1.next.next=ListNode(5)
nlist+=[n1]
n1=ListNode(1)
n1.next=ListNode(3)
n1.next.next=ListNode(4)
nlist+=[n1]
n1=ListNode(2)
n1.next=ListNode(6)
nlist+=[n1]
 
mh=s.mergeKLists([None])
while mh:
    print(mh.val)
    mh=mh.next
