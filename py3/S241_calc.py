'''
241. Different Ways to Add Parentheses
Medium

Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation: 
((2-1)-1) = 0 
(2-(1-1)) = 2

Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
'''
from __future__ import annotations
import itertools

class Solution:
    def diffWaysToCompute(self, input):    
        ops = {'+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y}
        def ways(s):
            ans = []
            for i in range(len(s)):
                if s[i] in "+-*":          
                    ans += [ops[s[i]](l, r) for l, r in itertools.product(ways(s[0:i]), ways(s[i+1:]))]
            if not ans: ans.append(int(s) if len(s) > 0 else 0 )
            return ans
        return ways(input)

s=Solution()
s.diffWaysToCompute("-2+3")