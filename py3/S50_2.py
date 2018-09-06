class Solution:
    def myPow(self, x, n):
        if n==0:
             return 1
        if n < 0:
            x = 1/x
            n = -n
        s=0
        a=[]
        while(n > 0):
            if n%2 == 1:
                a+=[s]
            s+=1
            n=n>>1
        r=1
        for i in a[::-1]:
            j=0
            xj=x
            while(j<i):
                xj=xj*xj
                j+=1
            r=r*xj
        return r

s=Solution()
print(s.myPow(2, 10))

