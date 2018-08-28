'''
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL

Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k):
        if head == None:
            return None
        len=0
        itr=head
        while True:
            len+=1
            if itr.next != None:
                itr = itr.next
            else:
                itr.next=head
                break
        c=(len-k%len)%len
        for i in range(c):
            itr = itr.next
        head=itr.next
        itr.next=None
        return head

s=Solution()
li=[ListNode(i) for i in range(1,6)]
for x in range(4):
    li[x].next=li[x+1]

r=s.rotateRight(li[0], 2)
while r != None:
    print(r.val)
    r=r.next