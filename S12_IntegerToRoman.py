# Given an integer, convert it to a roman numeral.
# Input is guaranteed to be within the range from 1 to 3999.
# Symbol 	I 	V 	X 	L 	C 	    D 	    M
# Value 	1 	5 	10 	50 	100 	500 	1000
class Solution:
    def intToRoman(self, num):
        rtype='M'*(num//1000)
        num%=1000
        rtype+='CM' if num//100 == 9 else ( 'CD' if num//100 == 4 else 'D'*(num//500) + 'C'*(num%500//100))
        num%=100
        rtype+='XC' if num//10 == 9 else ( 'XL' if num//10 == 4 else 'L'*(num//50) + 'X'*(num%50//10))
        num%=10
        rtype+='IX' if num == 9 else ( 'IV' if num == 4 else 'V'*(num//5) + 'I'*(num%5))
        return rtype


s=Solution()        
print(s.intToRoman(390))
print(s.intToRoman(80))
print(s.intToRoman(79))
print(s.intToRoman(60))
print(s.intToRoman(50))
print(s.intToRoman(40))
print(s.intToRoman(30))
print(s.intToRoman(4))