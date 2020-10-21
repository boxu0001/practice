'''
17. Letter Combinations of a Phone Number
Medium

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:

Input: digits = ""
Output: []

Example 3:

Input: digits = "2"
Output: ["a","b","c"]
'''
from __future__ import annotations
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numLetters=[[] for _ in range(10)] 
        charA=ord('a')
        j=0
        for i in range(2, 10):
            d=3
            if i == 7 or i==9:
                d=4
                
            for _ in range(d):
                numLetters[i] += [chr(charA+j)]
                j+=1

        result = None
        nums=[int(c) for c in digits]   
        while nums:
            ci = int(nums.pop(0))
            if result == None:
                result = numLetters[ci]
            else:
                tmp = []    #使用替换数组更高效
                for r in result:
                    for cc in numLetters[ci]:
                        tmp+=[r+cc]
                result = tmp

        return result

        
    
    def backtrack(self, numLetters, nums):
        if len(nums)==0:
            return []
        elif len(nums)==1:
            return numLetters[nums[0]]
        else:
            result=[]
            tmpRes = self.backtrack(numLetters, nums[1:])
            for c in numLetters[nums[0]]:
                for subList in tmpRes:
                    result+=[c+subList]
            
            return result

s=Solution()
s.letterCombinations('24')