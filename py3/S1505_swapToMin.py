'''
1505. Minimum Possible Integer After at Most K Adjacent Swaps On Digits
Hard

Given a string num representing the digits of a very large integer and an integer k.

You are allowed to swap any two adjacent digits of the integer at most k times.

Return the minimum integer you can obtain also as a string.

 

Example 1:

Input: num = "4321", k = 4
Output: "1342"
Explanation: The steps to obtain the minimum integer from 4321 with 4 adjacent swaps are shown.

Example 2:

Input: num = "100", k = 1
Output: "010"
Explanation: It's ok for the output to have leading zeros, but the input is guaranteed not to have any leading zeros.

Example 3:

Input: num = "36789", k = 1000
Output: "36789"
Explanation: We can keep the number without any swaps.

Example 4:

Input: num = "22", k = 22
Output: "22"

Example 5:

Input: num = "9438957234785635408", k = 23
Output: "0345989723478563548"

 

Constraints:

    1 <= num.length <= 30000
    num contains digits only and doesn't have leading zeros.
    1 <= k <= 10^9
'''

from __future__ import annotations
class Solution:

    def bitTreeUpdate(self, treee: list[int], idx: int, delta: int):
        idx += 1
        ls = len(treee)
        while idx < ls:
            treee[idx] += delta # log(n)
            idx += idx & (-idx)    
        
    
    def bitTreeSum(self, treee: list[int], idx: int) -> int:
        idx+=1
        ret = treee[idx]
        while idx > 0:
            idx -= idx & (-idx) #find parent idx    log(n)
            ret += treee[idx]
        return ret


    def minInteger(self, num: str, k: int) -> str:
        num=[int(s) for s in num]

        numidx = [[] for _ in range(10)]    #O(n)
        for i, s in enumerate(num):
            numidx[s] += [i]
        ls = len(num)

        bitTree = [0] * (ls+1) # one started bit tree
        result=[]
        count=0
        i=0
        while count < ls and k > 0:     #O(n)
            nbi = num[i]
            if nbi == None:
                i+=1
                continue

            found = False
            imoved = self.bitTreeSum(bitTree, i)        #O(log(n))
            for d, diqueue in enumerate(numidx):
                if d < nbi and diqueue and diqueue[0] - i - self.bitTreeSum(bitTree, diqueue[0]) + imoved <= k:     #O(log(n))
                    dix = diqueue.pop(0)
                    result+=[str(d)]
                    count+=1
                    k-=dix - i - self.bitTreeSum(bitTree, dix) + imoved
                    self.bitTreeUpdate(bitTree, dix, 1)
                    found=True
                    num[dix] = None
                    break
            if not found:
                result+=[str(num[i])]
                numidx[nbi].pop(0)
                num[i] = None
                count+=1
                i+=1
        
        for n in num:
            if n != None: result += [str(n)]
        return "".join(result)

    #以上解法使用 binary index tree or Fenwick Tree, Time O(nlog(n)), Space O(n)
    # tree(i) = function(parent(i), i), here function is sum
    # parent(i) = i - (i & (-i)) or i-(i&(~(i-1)))
    # for next j,  p(j) <= i < j,  j = i+(i&(-i))


    #以下解法使用简单的递归， 效率也很高
    def minInteger2(self, num: str, k: int) -> str:
        n=len(num)
        if k<=0:
            return num
        
        if k>n*(n-1)//2:
            return ''.join(sorted(list(num)))
        
        for i in range(10):
            idx = num.find(str(i))  # O(n)
            if idx>=0 and idx<=k:
                return num[idx]+self.minInteger(num[:idx]+num[idx+1:],k-idx)    #O(n)

        # Time O(n**2), Space O(n)

s=Solution()
# s.minInteger("4321", 4)
s.minInteger("36789", 5000)
# tree=[0]*17
# s.bitTreeUpdate(tree, 1, 1)
# s.bitTreeUpdate(tree, 8, 1)
# s.bitTreeUpdate(tree, 3, 1)
# print(tree)
# print(s.bitTreeSum(tree, 3))

