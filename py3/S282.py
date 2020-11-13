'''
282. Expression Add Operators
Hard

Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Example 1:

Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"] 

Example 2:

Input: num = "232", target = 8
Output: ["2*3+2", "2+3*2"]

Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]

Example 4:

Input: num = "00", target = 0
Output: ["0+0", "0-0", "0*0"]

Example 5:

Input: num = "3456237490", target = 9191
Output: []

 

Constraints:

    0 <= num.length <= 10
    num only contain digits.

'''

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        
        N=len(num)
        # 4 option, +-* and None
        result=[]
        # operator, 0=concat, 1='+', 2='-', 3='*'
        stack=[[0, 1, int(num[0]), 0]] if N > 0 else []  #entry, [prev value, multiply base, last number, next operator]
        
        while stack:
            prvVal, multiBase, lstNmb, nxtOpr = stack[-1]
            i=len(stack)
            
            if i == N or nxtOpr > 3:
                if i==N and prvVal + multiBase*lstNmb == target:
                    #print(stack)
                    res = num[0]
                    for d in range(N-1):
                        if stack[d][-1] == 0:
                            res+=num[d+1]
                        elif stack[d][-1] == 1:
                            res+="+" + num[d+1]
                        elif stack[d][-1] == 2:
                            res+="-" + num[d+1]
                        else:
                            res+="*" + num[d+1]
                    
                    result+=[res]

                stack.pop()
                if stack: stack[-1][-1]+=1 
            elif nxtOpr == 0 and lstNmb != 0:
                stack+=[[prvVal, multiBase, lstNmb*10+int(num[i]), 0]]
            elif nxtOpr == 0:   #lstNmb == 0, avoid concat after "0", eg. "09"
                stack[-1][-1]+=1
            elif nxtOpr == 1:
                stack+=[[prvVal+multiBase*lstNmb, 1, int(num[i]), 0]]
            elif nxtOpr == 2:
                stack+=[[prvVal+multiBase*lstNmb, -1, int(num[i]), 0]]
            else:
                stack+=[[prvVal, multiBase*lstNmb, int(num[i]), 0]]
        
        return result
