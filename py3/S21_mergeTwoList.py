# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Example:
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        tempHead=ListNode(0)            #定义零时头节点
        curHead=tempHead
        while l1 or l2:
            if l1 == None or (l2 != None and l1.val > l2.val):  #当l1到头了 或者 l1 , l2都没到头并且l1.val > l2.val, 
                curHead.next=l2                                 #移动 当前节点到l2, l2向前， 当前节点也向前
                l2=l2.next
                curHead=curHead.next
            else:                                               #逻辑上是 11!=None and (l2 == None or l1.val<=l2.val)
                curHead.next=l1
                l1=l1.next
                curHead=curHead.next
        return tempHead.next

#总结：用临时头节点会方便算法实现