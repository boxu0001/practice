'''
227. Basic Calculator II
Medium

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7

Example 2:

Input: " 3/2 "
Output: 1

Example 3:

Input: " 3+5 / 2 "
Output: 5

Note:

    You may assume that the given expression is always valid.
    Do not use the eval built-in library function.
'''
from __future__ import annotations
class Solution:
    def calculate(self, s: str) -> int:
        op = '+'
        stack = [] 
        s += '+'
        num = 0 
        for c in s: 
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in '+-/*':       #eg. 'A+B-', A on stack, op=='+', num==B, c=='-' 
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    prev = stack.pop() 
                    stack.append(num * prev)
                elif op == '/':
                    prev = stack.pop()
                    stack.append(int(prev / num))
                op = c
                num = 0
        return sum(stack)

s=Solution()
s.calculate('5*6')