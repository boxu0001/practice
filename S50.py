# Implement pow(x, n). 
class Solution:
    def myPow(self, x, n):
        if n==0:
             return 1
        if n < 0:
            x = 1/x
            n = -n
        r=1
        while(n > 0):
            if n%2 == 1:
                r=r*x
            x*=x    
            n=n>>1
        return r

s=Solution()
print(s.myPow(2, -10))

