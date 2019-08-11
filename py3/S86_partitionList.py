# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

# Example:

# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummyLT = ListNode(-1)
        dummyGE = ListNode(-1)
        itr = head
        itrLT = dummyLT
        itrGE = dummyGE
        while itr:
            if itr.val < x:
                itrLT.next = itr
                itr = itr.next
                itrLT = itrLT.next
                itrLT.next = None
            else:
                itrGE.next = itr
                itr = itr.next
                itrGE = itrGE.next
                itrGE.next = None
            
        itrLT.next = dummyGE.next
        return dummyLT.next
#使用了两个链表进行处理， 注意dummy head用法
#一个链接所有小于节点
#一个链接所有大于等于节点

    def partition2(self, head: ListNode, x: int) -> ListNode:
        firstGE=None
        firstGEPrev=None
        dummyHead=ListNode(-1)
        dummyHead.next=head
        itr=head
        itrPrev=dummyHead
        while itr != None:
            if itr.val >= x and firstGE == None:
                firstGE = itr                       #找到第一个大于等于的节点，作为分割点
                firstGEPrev=itrPrev
                itrPrev = itr
                itr = itr.next                
            elif itr.val < x and firstGE != None:   #之后遇到的小于节点，都移到分割点之前
                firstGEPrev.next = itr
                itrPrev.next = itr.next
                itr.next = firstGE
                firstGEPrev = itr
                itr = itrPrev.next                  
            else:                                   #剩余的情况是 1. 分割点没出现 而当前为小于的节点 2.或者分割点出现 当前为大于等于节点
                itrPrev = itr                       #这两种情况都不需要做处理
                itr = itr.next
        return dummyHead.next
#在原有链表上处理 注意dummy head用法


s=Solution()
head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
s.partition(head, 4)