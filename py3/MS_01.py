'''
You are give an array of numbers, you need to find out a pair of numbers whos sum is max and also the sum of digits are same.

ex: [60,42,35]

    Sum of digits in 60 =6. Sum of digits in 42 =6. Add both the digit sums, 6+6=12. Since greater than 10 reduce again. 1+2=3
    Sum of 60 +42= 102. 1+0+2=3
    Since number at step 1== step 2 if it is max value for the whole array return that value.

Another example : [42,33,60]
42+60 and 33+60 are 102 and 93 respectively, the sum of digits are same for both the pairs, return 102 since that is the max.
'''
from __future__ import annotations
class Solution:
    def findPair(self, numbers):
        map9 ={}
        for n in numbers:
            key = 9 if n%9 == 0 else n%9
            if key not in map9:
                map9[key] = []
            map9[key]+=[n]




            
            

