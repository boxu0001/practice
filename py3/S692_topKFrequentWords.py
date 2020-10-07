'''
692. Top K Frequent Words
Medium

Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:

Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:

Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.

Note:

    You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
    Input words contain only lowercase letters.

Follow up:

    Try to solve it in O(n log k) time and O(n) extra space.
'''
from __future__ import annotations
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        lens=len(words)
        wordcnt={}
        queue=[] #space O(k)
        
        for w in words:
            if w not in wordcnt:
                wordcnt[w] = 0
            else:
                wordcnt[w] +=1
        #time O(n)
        
        for w in wordcnt:
            newitem = (wordcnt[w], w)
            if len(queue) < k:
                self.pushqueue(queue, newitem)
            elif len(queue) == k and self.compareitems(queue[0], newitem) < 0:
                self.replacetop(queue, newitem)
            else:
                pass
        #time O(nlog(k))
        result=[]
        while queue:
            _, w = queue[0]
            result+=[w]
            if len(queue) > 1:
                self.replacetop(queue, queue.pop())
            else:
                break
            
        return result[::-1]
    
    def pushqueue(self, queue: List, item: (int, str)):
        queue+=[item]
        ci = len(queue)-1
        pi = (ci-1)//2
        while pi >=0:
            pitem = queue[pi]
            citem = queue[ci]
            if self.compareitems(citem, pitem) < 0:
                queue[ci] = pitem
                queue[pi] = citem
                ci = pi
                pi = (ci-1)//2
            else:
                break
        return

    def replacetop(self, queue: List, item: (int, str)):
        queue[0] = item
        pi = 0
        K = len(queue)
        while pi < K:
            c1 = pi*2+1
            c2 = pi*2+2
            small=c1 if c1 < K else None
            if c2 < K:
                small= c1 if self.compareitems(queue[c1], queue[c2]) < 0 else c2
            if small != None and self.compareitems(queue[small], queue[pi]) < 0:
                smallitem = queue[small]
                queue[small] = queue[pi]
                queue[pi] = smallitem
                pi = small
            else:
                break
        return

    def compareitems(self, item1, item2):
        (c_val, c_wd) = item1
        (p_val, p_wd) = item2
        if c_val < p_val or (c_val == p_val and c_wd > p_wd):
            return -1
        else:
            return 1
        

    # simply using heapq, NOTICE it's O(nlog(n))
    import heapq as pq
    def topKFrequent_simple(self, words: List[str], k: int) -> List[str]:
        lens=len(words)
        wordcnt={}
        queue=[]
        
        for w in words:
            if w not in wordcnt:
                wordcnt[w] = lens
            else:
                wordcnt[w] -=1
        
        for w in wordcnt:
            pq.heappush(queue, (wordcnt[w], w))
        
        result=[]
        for i in range(k):
            result+=[pq.heappop(queue)[1]]
        
        return result

s=Solution()
s.topKFrequent(["love", "leetcode", "a", "love", "coding", "a"], 2)
