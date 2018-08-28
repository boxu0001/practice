'''
The set [1,2,3,...,n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

    "123"
    "132"
    "213"
    "231"
    "312"
    "321"

Given n and k, return the kth permutation sequence.
Note:

    Given n will be between 1 and 9 inclusive.
    Given k will be between 1 and n! inclusive.

Example 1:
Input: n = 3, k = 3
Output: "213"

Example 2:
Input: n = 4, k = 9
Output: "2314"
'''
import math
class Solution:
    def getPermutation(self, n, k):
        f=[math.factorial(i) for i in range(1, n+1)]
        r=[str(i) for i in range(n+1)]
        z=[]
        for i in range(n):
            d=k//f[n-i-1]
            k=k%f[n-i-1]
            if k==0:
                z+=[r.pop(d-1)]
                z+=r[::-1]
                return "".join(z[1:])           
            else:
                z+=[r.pop(d)]
        return "".join(z[1:])

s=Solution()
for i in range(1, math.factorial(7)+1):
    print(s.getPermutation(7,i))
