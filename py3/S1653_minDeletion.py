'''
1653. Minimum Deletions to Make String Balanced
Medium

You are given a string s consisting only of characters 'a' and 'b'​​​​.

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.

 

Example 1:

Input: s = "aababbab"
Output: 2
Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").

Example 2:

Input: s = "bbaaaaabb"
Output: 2
Explanation: The only solution is to delete the first two characters.

 

Constraints:

    1 <= s.length <= 105
    s[i] is 'a' or 'b'​​.

'''

import collections
class Solution:
    def minimumDeletions2(self, s: str) -> int:
        cnts = collections.Counter(s)
        rema = cnts['a']
        remb = cnts['b']
        N=rema+remb
        
        maxCnt = 0
        cura, curb = 0, 0
        for c in s: 
            if c == 'b':        # (cura, curb) -- b -> (cura,curb+1), states changed
                curb+=1
                remb-=1
            else:
                maxCnt = max(maxCnt, cura + curb + remb)    #delete all remaining 'a', get one possible result, (cura, curb) -----> (cura, curb+remb) this is one final
                cura+=1     #or add the 'a' and removing leading 'b's,   (cura, curb) -- a -> (cura+1, 0)
                rema-=1
                curb=0
        
        maxCnt = max(maxCnt, cura+curb)
        return maxCnt
    
    def minimumDeletions(self, s: str) -> int:
        stack=[]
        cnt=0
        for c in s:
            if stack and stack[-1]=='b' and c == 'a':   # we don't know which one to delete, but we know there must be a deletion, the final string depends on remaining chars
                stack.pop()                             #for example, for  'ba' ->'?', 'bba' -> 'b?', 'baa' -> '?a', 'bababba' -> '??b?', we just need to count '?' 
                cnt+=1
            else:
                stack+=[c]
            
        return cnt
    
        
