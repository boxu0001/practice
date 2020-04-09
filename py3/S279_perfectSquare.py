'''
279. Perfect Squares
Medium

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''

class Solution:
    def numSquares(self, n: int) -> int:
        # step[i] = s means from "0" --> "i" needs s steps,
        # init "0" --> "0" needs 0 step
        step = set({0})
        cLevel=[0]
        cStep=0
        while True:
            nLevel=[]
            nStep=cStep+1
            for cNode in cLevel:
                i = 1
                while cNode + i*i <= n:
                    nNode = cNode + i*i
                    if nNode not in step:
                        nLevel+=[nNode]
                        step.add(nNode)
                        if nNode == n:
                            return nStep
                    i+=1
            cLevel=nLevel
            cStep=nStep
            
        return None
    
    #following using Lagrange Four Square theorem
    def numSquaresLagrange4Square(self, n: int):
        if (n**0.5).is_integer():
            return 1
        sqr = int(n**0.5)
        for i in range(1,sqr+1):
            if ((n - i*i)**0.5).is_integer():
                return 2
        
        # (4**i)(8k+7) must be 4 
        while (n/4).is_integer():
            n= n/4
        if n%8 == 7:
            return 4
        else:
            return 3

s=Solution()
println(s.numSquares(13))