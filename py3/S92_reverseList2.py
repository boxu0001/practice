# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy=ListNode(-1)
        dummy.next=head
        headPrev=None
        tail=None
        itr=dummy
        itrNext=head
        cnt=0
        while cnt <= n:
            if cnt == m-1: headPrev = itr
            if cnt == n: tail = itr
            if m<=cnt<n:
                itrNextNext = itrNext.next if itrNext else None
                itrNext.next = itr
                itr = itrNext
                itrNext = itrNextNext
            else:
                itr = itrNext
                itrNext=itrNext.next
            cnt+=1
            
        headPrev.next.next=itr
        headPrev.next=tail
        
        return dummy.next

    def reverseBetween2(self, head: ListNode, m: int, n: int) -> ListNode:
        
        dummy = ListNode(0)
        dummy.next = head
        
        cur, prev = head, dummy 
        for _ in range(m - 1):  #把 cur 移动 m-1次， 到第m个节点
            cur = cur.next
            prev = prev.next
        
        #之后 cur , prev将不会在移动了， cur为新的尾节点 （第m个节点）， 这里用 prev.next 和 cur.next 为变量
        for _ in range(n - m):  
            temp = cur.next             #temp被移动 n-m次， 遍历 m+1， m+2, ..., n (m+n-m)节点
            cur.next = temp.next        #注意这里用cur.next 指向下一个temp， 最后指向最终链接节点(n+1), 
            temp.next = prev.next       #改变链接方向
            prev.next = temp            #prev.next 最后指向最终改变后头节点（第n个节点）

        return dummy.next

hd=ListNode(1)
hd.next=ListNode(2)
hd.next.next=ListNode(3)
hd.next.next.next=ListNode(4)
hd.next.next.next.next=ListNode(5)
s=Solution()
s.reverseBetween(hd,2,4)
