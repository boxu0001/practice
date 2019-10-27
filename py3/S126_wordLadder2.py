'''
126. Word Ladder II
Hard

Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

    Only one letter can be changed at a time
    Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

Note:

    Return an empty list if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.
    You may assume no duplicates in the word list.
    You may assume beginWord and endWord are non-empty and are not the same.

Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]

Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
'''

from __future__ import annotations
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        lenw=len(beginWord)
        dist={beginWord:0}
        queue=[beginWord]
        alpha='abcdefghijklmnopqrstuvwxyz'
        while queue:
            curWd = queue.pop(0)
            for i in range(lenw):
                for nxtWd in [curWd[:i]+c+curWd[i+1:] for c in alpha]:
                    if nxtWd not in dist and nxtWd in wordSet:
                        dist[nxtWd] = dist[curWd]+1
                        queue+=[nxtWd]
                        if nxtWd == endWord:
                            break
        
        if endWord not in dist:
            return []
        
        result=[[endWord]]
        for i in range(dist[endWord]-1, -1, -1):
            tmp=result
            result=[]
            for li in tmp:
                for k in range(lenw):
                    for prvWd in [li[0][:k]+c+li[0][k+1:] for c in alpha]:
                        if prvWd in dist and dist[prvWd] == i:
                            result+=[[prvWd] + [_ for _ in li]]

        return result



s=Solution()
s.findLadders(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"])