'''
336. Palindrome Pairs
Hard

Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.

 

Example 1:

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]

Example 2:

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]

Example 3:

Input: words = ["a",""]
Output: [[0,1],[1,0]]

 

Constraints:

    1 <= words.length <= 5000
    0 <= words[i] <= 300
    words[i] consists of lower-case English letters.
'''
from __future__ import annotations
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = {}
        N=len(words)
        emptyIdx = None
        for wid, w in enumerate(words):
            if w == "":
                emptyIdx = wid
            else:
                self.buildTrie(w[::-1], wid, trie)

        result=[]
        if emptyIdx != None:
            for mid in trie["ID"]:
                result+=[[emptyIdx, mid], [mid, emptyIdx]]


        for wid, w in enumerate(words):
            itr = trie
            i = 0

            while i < len(w):
                if "END" in itr and self.isPD(w[i:]) and itr["END"] != wid:
                    result += [[wid,itr["END"]]]

                if w[i] in itr:
                    itr = itr[w[i]]
                else: #w[i] not in itr
                    break
                i+=1

            if i==len(w) and i != 0:
                result += [[wid,mid] for mid in itr["ID"] if mid != wid]
            
        return result
                                 
      
    def buildTrie(self, w, id, trie):
        if self.isPD(w):
            if "ID" not in trie:
                trie["ID"] = {id}
            else:
                trie["ID"].add(id)
            
        for i, c in enumerate(w):
            if c not in trie:
                trie[c]={}
            trie = trie[c]
            if self.isPD(w[i+1:]):
                if "ID" not in trie:
                    trie["ID"] = {id}
                else:
                    trie["ID"].add(id)
        trie["END"] = id

    def isPD(self, w):
        n = len(w)
        i = 0
        j = n-1
        result=True
        while i <= j:
            if w[i] != w[j]:
                result=False
                break
            i+=1
            j-=1
        return result

s=Solution()
s.palindromePairs(["a","aa"])