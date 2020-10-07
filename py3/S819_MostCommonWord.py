'''
819. Most Common Word
Easy

Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.

 

Example:

Input: 
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.

 

Note:

    1 <= paragraph.length <= 1000.
    0 <= banned.length <= 100.
    1 <= banned[i].length <= 10.
    The answer is unique, and written in lowercase (even if its occurrences in paragraph may have uppercase symbols, and even if it is a proper noun.)
    paragraph only consists of letters, spaces, or the punctuation symbols !?',;.
    There are no hyphens or hyphenated words.
    Words only consist of letters, never apostrophes or other punctuation symbols.

'''

from __future__ import annotations
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        lns = len(paragraph)
        ignored={' ', '!', '?', '\'', ',',';','.'}
        banned=set(banned)
        words={}
        ei=0
        si=0    
        maxc=0
        maxw=None
        
        while True:
            if si < lns and paragraph[si] in ignored:
                si+=1
            elif ei < si:
                ei = si
            elif ei < lns and paragraph[ei] not in ignored:
                ei+=1
            elif si < ei:
                #find a word
                w=paragraph[si:ei].lower()
                if w not in banned:
                    if w not in words:
                        words[w]=1
                    else:
                        words[w]+=1
                    if words[w] > maxc:
                        maxc = words[w]
                        maxw = w
                si=ei
                
            else:
                break        
        return maxw

    #second solution using RE
    import re
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        words=re.split(r'[!?\';,.\s]+', paragraph.lower())
        cached={}
        maxc=0
        maxw=None
        for w in words:
            if w not in banned and w != '':
                if w not in cached:
                    cached[w]=1
                else:
                    cached[w]+=1
                if cached[w] > maxc:
                    maxc = cached[w]
                    maxw = w
        return maxw        

s=Solution()
s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])