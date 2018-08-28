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
    def mergeKLists(self, lists):    
        pqList = []
        for ni in lists:
            if ni != None:
                self.addNode(ni, pqList)
                
        if len(pqList) == 0:
            return None

        result = ListNode(0)
        itr = result
        while len(pqList) > 1:
            poped = pqList[0]
            itr.next = poped
            itr = itr.next

            if poped.next != None:
                pqList[0] = poped.next
            else:
                last = pqList.pop()
                pqList[0] = last
            self.topDownNode(pqList)    


        itr.next = pqList[0] 
        return result.next
            
    def addNode(self,node,pqList):
        pqList += [node]
        parentI = len(pqList)//2-1
        currentI = len(pqList)-1
        while parentI >= 0 and pqList[parentI].val > node.val:
            #swap parent
            pqList[currentI] = pqList[parentI]
            pqList[parentI] = node
            currentI = parentI
            parentI = (currentI-1)//2
        return pqList

    def topDownNode(self, pqList):
        ls = len(pqList)
        if len(pqList) == 0:
            return
        currentI = 0
        leftI = 2 * currentI + 1 if 2 * currentI + 1 < ls else currentI
        rightI = 2 * currentI + 2 if 2 * currentI + 2 < ls else currentI 
        while currentI < ls and pqList[currentI].val > min(pqList[leftI].val, pqList[rightI].val):
            minI = leftI if pqList[leftI].val < pqList[rightI].val else rightI
            node = pqList[currentI]
            pqList[currentI] = pqList[minI]
            pqList[minI] = node
            currentI = minI
            leftI = 2 * currentI + 1 if 2 * currentI + 1 < ls else currentI
            rightI = 2 * currentI + 2 if 2 * currentI + 2 < ls else currentI 

        return pqList

s=Solution()

l=[
    [1,4,5],
    [1,3,4],
    [2,6],
    [9]
]

nodeL = []
for ni in l:
    if len(ni) > 0:
        ro = ListNode(ni[0])
        nli = ro
        for j in ni[1:]:
            nli.next = ListNode(j)
            nli=nli.next
        nodeL += [ro]

r = s.mergeKLists(nodeL)
while r != None:
    print(r.val)
    r = r.next


# plist=[]
# s.addNode(ListNode(9), plist)
# s.addNode(ListNode(8), plist)
# s.addNode(ListNode(7), plist)
# s.addNode(ListNode(6), plist)
# s.addNode(ListNode(5), plist)
# s.addNode(ListNode(2), plist)
# s.addNode(ListNode(3), plist)
# s.addNode(ListNode(4), plist)
# s.addNode(ListNode(1), plist)
# for i in plist:
#     print(i.val)

# while len(plist) > 0:
#     print("->", plist[0].val)
#     if len(plist) > 0:
#         plist[0]=plist.pop()
#         s.topDownNode(plist)
