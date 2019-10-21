'''
1223. Dice Roll Simulation
Medium

A die simulator generates a random number from 1 to 6 for each roll. You introduced a constraint to the generator such that it cannot roll the number i more than rollMax[i] (1-indexed) consecutive times. 

Given an array of integers rollMax and an integer n, return the number of distinct sequences that can be obtained with exact n rolls.

Two sequences are considered different if at least one element differs from each other. Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: n = 2, rollMax = [1,1,2,2,2,3]
Output: 34
Explanation: There will be 2 rolls of die, if there are no constraints on the die, there are 6 * 6 = 36 possible combinations. In this case, looking at rollMax array, the numbers 1 and 2 appear at most once consecutively, therefore sequences (1,1) and (2,2) cannot occur, so the final answer is 36-2 = 34.

Example 2:

Input: n = 2, rollMax = [1,1,1,1,1,1]
Output: 30

Example 3:

Input: n = 3, rollMax = [1,1,1,2,2,3]
Output: 181

 

Constraints:

    1 <= n <= 5000
    rollMax.length == 6
    1 <= rollMax[i] <= 15
'''

from __future__ import annotations

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        md=10**9+7
        ftn=[[0] for _ in range(6)]
        f=[1]
        for ni in range(1, n+1):
            f+=[0]
            for ti,t in enumerate(rollMax):
                ftn[ti]+=[0]
                if ni <= t:
                    ftn[ti][ni] = f[ni-1]
                elif ni > t > 0:
                    ftn[ti][ni] = (f[ni-1]-f[ni-t-1]+ftn[ti][ni-t-1])%md
                else:
                    ftn[ti][ni] = 0
                f[ni] = (f[ni] + ftn[ti][ni]) % md
        return f[n]

s=Solution()
s.dieSimulator(2, [1,1,1,1,1,1])
