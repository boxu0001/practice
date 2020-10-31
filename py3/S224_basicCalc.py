'''
224. Basic Calculator
Hard

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2

Example 2:

Input: " 2-1 + 2 "
Output: 3

Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23

Note:

    You may assume that the given expression is always valid.
    Do not use the eval built-in library function.
'''
class Solution:
    def calculate(self, s: str) -> int:
        N=len(s)
        result=0
        operands=[]
        operator=[]
        i=0
        while i < N:
            c=s[i]
            if c.isdigit():
                j=i+1
                while j<N and s[j].isdigit():
                    j+=1 
                print(s[i:j])
                operands+=[int(s[i:j])]
                self.calc(operands, operator)
                i=j
                continue
            elif c == "+" or c == "-":
                operator+=[c]
            elif c == "(":
                operands+=[c]
            elif c == ")": #pop
                if operands:
                    op1 = operands.pop()
                    if operands and operands[-1] == '(':
                        _ = operands.pop()
                    operands+=[op1]
                    self.calc(operands, operator)
            else:
                pass
            
            i+=1
        return operands[-1]
            
    def calc(self, operands, operator):
        while len(operands) >= 2 and operands[-1] != "(" and operands[-2] != "(" and len(operator) > 0:
            op1 = operands.pop()
            op2 = operands.pop()
            opr = operator.pop()
            if opr == "+":
                operands+=[int(op2)+int(op1)]
            else:
                operands+=[int(op2)-int(op1)]

s=Solution()
s.calculate("2147483647")