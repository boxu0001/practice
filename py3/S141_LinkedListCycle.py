'''
141. Linked List Cycle
Easy

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow=head
        fast=head.next if head else None
        while fast:
            if fast == slow:
                return True
            fast = fast.next.next if fast.next else None
            slow = slow.next
        return False

# fast向前两步
# slow向前一步
#如果有cycle,fast一定会遇到slow, 
#这里"一定遇到" 满足所有条件，
#  如果， f -> s -> _, 那么下一个循环， _ -> _ -> f/s
#  如果， f -> _ -> s -> _, 那么下个循环， _ -> _ -> f -> s, 为上一种情况

