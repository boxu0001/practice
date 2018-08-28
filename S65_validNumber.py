# 65. Valid Number
# DescriptionHintsSubmissionsDiscussSolution

# Validate if a given string is numeric.

# Some examples:
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true

# Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.

import re
class Solution:
    def isNumber(self, s):
        p=re.compile('^[-+]?[\d]*(\.\d|\d\.|\d)[\d]*$|^[-+]?[\d]*(\.\d|\d\.|\d)[\d]*[e|E]{1}[-+]?[\d]+$')
        m=p.match(s.strip())
        return False if m == None else True
s=Solution()
print(s.isNumber(""))
print(s.isNumber("."))
print(s.isNumber("-"))
print(s.isNumber("-1."))
print(s.isNumber("-.1"))
print(s.isNumber("-.1"))
print(s.isNumber("-.1e"))
print(s.isNumber("-1.e"))
print(s.isNumber("-.1e1"))
print(s.isNumber("-1.e1"))
print(s.isNumber("3.5e+3.5e+3.5"))