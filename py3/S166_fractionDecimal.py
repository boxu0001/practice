'''
166. Fraction to Recurring Decimal
Medium

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"

Example 2:

Input: numerator = 2, denominator = 1
Output: "2"

Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"
'''

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        negative=numerator//denominator < 0
        numerator = abs(numerator)
        denominator = abs(denominator)
        intpart = str(numerator//denominator)
        m = numerator%denominator
        r=[]
        mm = {}
        initMod=None
        repeatIdx = None
        while True:
            if m == 0:
                break
            m = m*10
            if m not in mm:
                i = m//denominator
                r+=[str(i)]
                mm[m] = len(r) - 1
                m = m%denominator
            else:
                repeatIdx = mm[m]
                break
        result = intpart if not negative else '-'+intpart
        if len(r) > 0:
            result+='.'
            for i, d in enumerate(r):
                if i == repeatIdx:
                    result+='('
                result+=d
            if repeatIdx != None:
                result+=')'
        
        return result
        
        