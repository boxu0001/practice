# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

# Example 1:
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"

# Example 2:
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[-1]
        result=0
        for i,c in enumerate(s):
            if stack[-1]>=0 and s[stack[-1]]=='(' and c==')':
                si=stack.pop()
                result = max(result, i-stack[-1])
            else:
                stack+=[i]
        return result
            
#Note:
#1. we pop the stack once encounting closed parenthese '(' is paired with ')'
#2. once poped, the top one stack[-1] is the latest non-closed index, then we know from 'stack[-1] + 1' to 'i' is a valid substring
# and its length is 'i-stack[-1]', 
#3. we just need to find the max(i-stack[-1]) each time encounting closed parenthese
