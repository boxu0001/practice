# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        itr=head
        i=0
        dummyHead=ListNode(-1)
        dummyHead.next=head
        iprevStart=dummyHead        #before reversed, it will be the end after reverse
        A=None
        B=None
        C=None
        while itr:
            if i%k==0:
                A=itr
                B=A.next if A else None
                C=B.next if B else None
                itr=itr.next
            elif i%k==k-1:
                for j in range(k-1):        #这里做reverse
                    B.next=A
                    A=B
                    B=C
                    C=C.next if C else None   
                iCurrStart=iprevStart.next  #由上一次的初始化推出， before reversed start, 
                iCurrStart.next=B           #然后初始化下次循环需要的尾节点
                iprevStart.next=A           #上一次的尾节点链接到当前K反转后的首节点， 完成之前和当前的链接
                iprevStart=iCurrStart       #继续

                itr=B
            else:
                itr=itr.next            
            i+=1
            
        return dummyHead.next

h=ListNode(1)
h.next=ListNode(2)
h.next.next=ListNode(3)
h.next.next.next=ListNode(4)
h.next.next.next.next=ListNode(5)
s=Solution()
nh=s.reverseKGroup(h, 3)
while nh:
    print(nh.val)
    nh=nh.next
