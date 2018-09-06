# Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
# Example:
# Input: 3
# Output:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]


class Solution:
    def generateMatrix(self, n):
        si=1
        result=[]
        s=[]
        e=[]
        for i in range(1, (n+1)//2+1):
            si+=4*(n-2*i+3) if i > 1 else 0
            ei=si+4*(n-2*i+1)-1
            s+=[si]
            e+=[ei]
            result+=[[e[j-1]-i+j+1 for j in range(1, i)] + [si+j-i for j in range(i, n-i+2)] + [s[n-j]+i+3*j-2*n-2 for j in range(n-i+2, n+1)]]
        for i in range((n+1)//2+1, n+1):
            result+=[[e[j-1]-i+j+1 for j in range(1, n-i+1)] + [e[n-i]-n+2*(n-i+1)-j for j in range(2*i-n)] + [s[n-j]+i+3*j-2*n-2 for j in range(i+1, n+1)]]                                    
        return result


s=Solution()
print(s.generateMatrix(2))
print(s.generateMatrix(3))
print(s.generateMatrix(4))
print(s.generateMatrix(5))