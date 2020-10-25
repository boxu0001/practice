'''
301. Remove Invalid Parentheses
Hard

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]

Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]

Example 3:

Input: ")("
Output: [""]
'''
from __future__ import annotations
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def countLR(s: str):
            l=0 #count invalid left parentheses
            r=0 #count invalid right parentheses
            for i, c in enumerate(s):
                if l > 0 and c==')':
                    l-=1
                elif c==')':
                    r+=1
                elif c=='(':
                    l+=1
                else:
                    pass
            return (l,r)
        
        l,r=countLR(s)
        result=[s] if l==0 and r==0 else []
        
        n = len(s)
        stack=[-1] if l>0 or r>0 else []
        lrem, rrem, nxti = l,r,0
        while stack:

            if rrem == 0 and lrem == 0: #satisfiy
                tmpS=""
                for xi in range(1, len(stack)):
                    tmpS+=s[stack[xi-1]+1:stack[xi]]
                    if xi == len(stack)-1:
                        tmpS+=s[stack[xi]+1:]
                
                li, ri = countLR(tmpS)
                if li == ri == 0:
                    result += [tmpS]

            if (rrem == 0 and lrem == 0) or nxti >= n:  #pop conditions
                nxti=stack.pop()
                if s[nxti] == '(':
                    lrem+=1
                else:
                    rrem+=1
                nxti+=1
                while nxti < n and s[nxti] == s[nxti-1]:    #to avoid duplicates, eg, s[stack[-1]]="(", we want to avoid next the same "(", 
                                                            #"(((XX", if poped is 0, we want to avoid 1 and 2
                    nxti+=1

                continue
            
            if rrem > 0:            #push condition, right paranthese first, to avoid illegal combination, 
                if s[nxti] == ')':
                    stack+=[nxti]
                    nxti+=1
                    rrem-=1
                else:
                    nxti+=1
            elif lrem > 0:          #then left,
                if s[nxti] == '(':
                    stack+=[nxti]
                    lrem-=1
                    nxti+=1
                else:
                    nxti+=1
                    
        if not result:        
            result=[""]            
            
        return result
        
                
s=Solution()
s.removeInvalidParentheses(")d))")