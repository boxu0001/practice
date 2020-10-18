from __future__ import annotations
class Solution:
    def maxSeq(self, num: int, low: int, upper: int) -> list[int]:
        n = upper - low + 1
        if num > 2 * n - 1:
            return -1
        
        result = []

        if num <= n:
            result+=[upper-1]
            for i in range(num-1):
                result+=[upper-i]
        else:   #num > n
            si = n - (num-n)
            for i in range(si, upper):
                result+=[i]
            for j in range(n):
                result+=[upper-j]

        return result

s=Solution()
s.maxSeq(3, 1, 2)
