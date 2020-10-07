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
import heapq as pq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        lens=len(words)
        wordcnt={}
        queue=[] #space O(n)
        
        for w in words:
            if w not in wordcnt:
                wordcnt[w] = lens
            else:
                wordcnt[w] -=1
        #time O(n)
        
        for w in wordcnt:
            pq.heappush(queue, (wordcnt[w], w))
        #time O(nlog(n))

        result=[]
        for i in range(k):
            result+=[pq.heappop(queue)[1]]
        
        return result
s=Solution()
s.topKFrequent(["love", "leetcode", "a", "love", "coding", "a"], 2)
