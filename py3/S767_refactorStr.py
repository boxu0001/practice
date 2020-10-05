'''
767. Reorganize String
Medium

Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"

Example 2:

Input: S = "aaab"
Output: ""

Note:

    S will consist of lowercase letters and have length in range [1, 500].
'''

class Solution:
    def reorganizeString(self, S: str) -> str:
        result=""
        count={}
        ln=len(S)
        maxC = None
        maxCnt = 0
        for c in S:
            if c in count:
                count[c]+=1
            else:
                count[c]=1
            if count[c] > maxCnt:
                maxC = c
                maxCnt = count[c]
            
        if ln - maxCnt < maxCnt -1: #抽屉原理，找到最多的character, 并算出需要多少抽屉， pigeon hole
            return result
        
        rs=[[maxC] for _ in range(maxCnt)]  
        count.pop(maxC)             
        j=0             #把剩下的char‘均匀’分配到抽屉中，相同char必须在不同draw里
        for key in count.keys():
            for i in range(count[key]):
                rs[j]+=[key]
                j=(j+1)%maxCnt
        
        for draw in rs:
            result += ''.join(draw)
        
        return result
        