
from __future__ import annotations
class Solution:
    # target is a string, len(target) <= 100000, split them in prime numbers, in order, fully consumerd, 
    # each prime number between [2, 1000000]

    def __init__(self):
        self.allPrims={2,3,5,7}
        self.MAXP = 1000000
        self.BASE = 1000000007

        for i in range(9, int(self.MAXP**0.5), 2):
            isPrime = True
            for a in self.allPrims:
                if i % a == 0:
                    isPrime = False
            if isPrime:
                self.allPrims.add(i)        

    def isPrime(self, n):
        if n == 1 or n == 0:
            return False
        if n in self.allPrims:
            return True
        res = True
        for p in self.allPrims:
            if n%p==0:
                res=False
                break
        return res
        
    def countPrimeStrings(self, target: str) -> int:
        N=len(target)
        m5=[[0]*N for _ in range(N)]
        f=[0]*(N+1)
        pln=len(str(self.MAXP))
        for d in range(1, pln):
            for i in range(0, N-d+1):
                j=i+d-1
                m5[i][j] = 1 if self.isPrime(int(target[i:j+1])) else 0

        f[0] = 1
        for i in range(0, N):
            for d in range(1, pln):
                #i+1-d from i, i-1, i-2, i-3, i-4, i-5
                if N > i+1-d >= 0:
                    f[i+1] += f[i+1-d]* m5[i+1-d][i] % self.BASE
                    
        return f[N]

#这里用dp, f(n) = f(n-1)*m5[n-1][n-1] + f(n-2)*m5[n-2:n-1] ..., index is inclusive here,  m5[i][j] states for target[i:j+1] is prime or not

s=Solution()

# s.countPrimeStrings("73")
s.countPrimeStrings("11373")
