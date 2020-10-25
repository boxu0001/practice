'''
996. Number of Squareful Arrays
Hard

Given an array A of non-negative integers, the array is squareful if for every pair of adjacent elements, their sum is a perfect square.

Return the number of permutations of A that are squareful.  Two permutations A1 and A2 differ if and only if there is some index i such that A1[i] != A2[i].

 

Example 1:

Input: [1,17,8]
Output: 2
Explanation: 
[1,8,17] and [17,8,1] are the valid permutations.

Example 2:

Input: [2,2,2]
Output: 1

 

Note:

    1 <= A.length <= 12
    0 <= A[i] <= 1e9
'''
import collections
class Solution:

    #following using DP, 
    def numSquarefulPerms(self, A: List[int]) -> int:
        A=sorted(A)
        N=len(A)
                
        f=[[0]*(1<<N) for _ in range(N)]
        
        for i in range(N):  #initialize
            f[i][0]=1       
            for j in range(i+1, N):
                if A[i]+A[j]==(int((A[i]+A[j])**0.5))**2:
                    f[i][(1<<i)|(1<<j)]=1
                    f[j][(1<<i)|(1<<j)]=1
        
        for ctn in range(1<<N): #containing bits
            ctnIdx=[i for i in range(N) if ((1<<i)&ctn) > 0]
            for hd in range(N):
                if ctn & (1<<hd) > 0:   # containing hd bit already, ignore
                    continue
                if hd == 0 or A[hd] != A[hd-1]:
                    for i, idx in enumerate(ctnIdx):
                        if i == 0 or A[ctnIdx[i]] != A[ctnIdx[i-1]]:
                            f[hd][ctn|(1<<hd)]+=f[hd][(1<<hd|1<<idx)] * f[idx][ctn]
                elif A[hd] == A[hd-1] :
                    f[hd][ctn|(1<<hd)]=f[hd-1][ctn|(1<<(hd-1))]
                else:
                    pass
                    
        result=0
        ctnAll=(1<<N)-1
        for i in range(N):
            if i==0 or A[i] != A[i-1]:
                result+=f[i][ctnAll]
        
        return result

    #following using DFS, recursion, polynomial, O(N!)
    
    def numSquarefulPerms2(self, A: List[int]) -> int:
        counts = collections.Counter(A)
        
        candidates = {i : {j for j in counts if int( (i + j)**0.5 )**2 == i + j} for i in counts}
        
        def dfs(x, used = 1):
            if used == len(A):
                return 1
            if used > len(A):
                return 0
            res = 0
            counts[x] -= 1
            for y in candidates[x]:
                if counts[y] > 0:
                    res += dfs(y, used + 1)
            counts[x] += 1
            return res
            # pass
        
        cnt = 0
        for x in counts:
            cnt += dfs(x)
        return cnt
        
