'''
943. Find the Shortest Superstring
Hard

Given an array A of strings, find any smallest string that contains each string in A as a substring.

We may assume that no string in A is substring of another string in A.
 

Example 1:

Input: ["alex","loves","leetcode"]
Output: "alexlovesleetcode"
Explanation: All permutations of "alex","loves","leetcode" would also be accepted.

Example 2:

Input: ["catg","ctaagt","gcta","ttca","atgcatc"]
Output: "gctaagttcatgcatc"

 

Note:

    1 <= A.length <= 12
    1 <= A[i].length <= 20
'''
from __future__ import annotations
class Solution:
    def shortestSuperstring(self, A: List[str]) -> str:
        lens=len(A)
        overlap=[[0]*lens for _ in range(lens)]
        for i, a in enumerate(A):
            for j, b in enumerate(A):
                for d in range(len(b), -1, -1):
                    if a.endswith(b[:d]):   #d is number of chars overlapped
                        overlap[i][j]= d 
                        break
        
        f=[[None]*(lens) for _ in range(1<<lens)]    #eg. f[31][3]=24,  31 binary = '11111', 3 is head, containing 1,2,3,4,5 words, min length is 24, 
        p=[[None]*(lens) for _ in range(1<<lens)]    # parent p[32][3] = 2, 3 connect to 2
       
        for i in range(lens):
            f[1<<i][i] = len(A[i])

        for s in range(2, 1<<lens):
            for wi in range(lens):
                if s & (1<<wi) > 0: # containing A[wi], eg wi=3, s=1101, containing A[0],A[2],A[3]
                    ps = s & ~(1<<wi) #parent state with wi removed, ps = 101, containing A[0],A[2]
                    for i in range(lens):
                        if f[ps][i] != None:
                            if f[s][wi] == None or f[ps][i] + len(A[wi]) - overlap[i][wi] < f[s][wi]:
                                f[s][wi] = f[ps][i] + len(A[wi]) - overlap[i][wi]
                                p[s][wi] = i
        
        
        state=(1<<lens)-1
        minLen = f[-1][0]
        xi=0
        for i, l in enumerate(f[-1]):
            if l < minLen:
                minLen=l
                xi = i
            
        result=A[xi]
        while p[state][xi] != None:
            pi = p[state][xi]
            result= A[pi][:len(A[pi])-overlap[pi][xi]] + result
            state = state & ~(1<<xi)
            xi = pi            
        return result


s=Solution()
print(s.shortestSuperstring(["DKKKABC","ABCKKKE","BCLLAB"]))
