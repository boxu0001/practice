'''
842. Split Array into Fibonacci Sequence
Medium

Given a string S of digits, such as S = "123456579", we can split it into a Fibonacci-like sequence [123, 456, 579].

Formally, a Fibonacci-like sequence is a list F of non-negative integers such that:

    0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type);
    F.length >= 3;
    and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.

Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.

Example 1:

Input: "123456579"
Output: [123,456,579]

Example 2:

Input: "11235813"
Output: [1,1,2,3,5,8,13]

Example 3:

Input: "112358130"
Output: []
Explanation: The task is impossible.

Example 4:

Input: "0123"
Output: []
Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.

Example 5:

Input: "1101111"
Output: [110, 1, 111]
Explanation: The output [11, 0, 11, 11] would also be accepted.

Note:

    1 <= S.length <= 200
    S contains only digits.

'''
from __future__ import annotations
class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        N = len(S)
        res=[]
        mx = 2 if N > 0 and S[0] == '0' else N//2+1
        for x in range(1, mx):
            my = x+2 if x+2 <= N and S[x] == '0' else N+1
            for y in range(x+1, my):
                f0=S[:x]
                f1=S[x:y]
                f2=str(int(f0)+int(f1))
                nxti = y
                tmp=[]
                while nxti+len(f2) <= N and f2 == S[nxti:nxti+len(f2)]:
                    #push
                    nxti+=len(f2)
                    tmp+=[int(f2)]
                    f0=f1
                    f1=f2
                    f2=str(int(f0)+int(f1))

                    if nxti == N:
                        res=[int(S[:x]), int(S[x:y])] + tmp
                        return res
        return res

s=Solution()
s.splitIntoFibonacci("539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511")