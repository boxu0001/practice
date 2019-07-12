# 24. Swap Nodes in Pairs
# Medium

# Given a linked list, swap every two adjacent nodes and return its head.
# You may not modify the values in the list's nodes, only nodes itself may be changed.

# Example:
# Given 1->2->3->4, you should return the list as 2->1->4->3.



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummyHead=ListNode(-1)
        dummyHead.next = head
        preHead=dummyHead
        curHead=head
        nxtHead=curHead.next if curHead else None   #注意末尾情况
        while nxtHead:
            curHead.next=nxtHead.next
            preHead.next=nxtHead
            nxtHead.next=curHead
            preHead = curHead
            curHead = curHead.next
            nxtHead = curHead.next if curHead else None #注意末尾情况
        
        return dummyHead.next
#注意边界条件， None node, 一个node的情况
#每次循环 把 preHead --> curHead --> nxtHead --> NEXT 变成 preHead --> nxtHead --> curHead --> NEXT



s=Solution()
hd=ListNode(1)
hd1=s.swapPairs(hd)
while hd1:
    print(hd1.val)
    hd1=hd1.next
hd.next=ListNode(2)
hd=s.swapPairs(hd)
while hd:
    print(hd.val)
    hd=hd.next