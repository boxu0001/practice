# 8. String to Integer (atoi)
# Medium

# Implement atoi which converts a string to an integer.

# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

# If no valid conversion could be performed, a zero value is returned.

# Note:

#     Only the space character ' ' is considered as whitespace character.
#     Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

# Example 1:

# Input: "42"
# Output: 42

# Example 2:

# Input: "   -42"
# Output: -42
# Explanation: The first non-whitespace character is '-', which is the minus sign.
#              Then take as many numerical digits as possible, which gets 42.

# Example 3:

# Input: "4193 with words"
# Output: 4193
# Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

# Example 4:

# Input: "words and 987"
# Output: 0
# Explanation: The first non-whitespace character is 'w', which is not a numerical 
#              digit or a +/- sign. Therefore no valid conversion could be performed.

# Example 5:

# Input: "-91283472332"
# Output: -2147483648
# Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
#              Thefore INT_MIN (−231) is returned.

class Solution:
    def myAtoi(self, stri: str) -> int:
        INT_MIN=-2147483648
        INT_MAX=2147483647
        state=[0,1,2]               #start=0, s1=1, end=2
        space=[i for i in range(6)] #space=0, '+-d'=1, 'other'=2, 'd'=3, 'non-d'=4, 'any char'=5 ,
        trs=[[None, None, None, None, None, None] for i in range(3)]
        trs[0][0]=0
        trs[0][1]=1
        trs[0][2]=2
        trs[1][3]=1
        trs[1][4]=2
        trs[2][5]=2
        num=''
        curState=0
        dSet = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        dSetPM = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-'}
        for s in stri:
            if curState == 0:
                sp=0 if s==' ' else 1 if s in dSetPM else 2
                curState=trs[curState][sp]
                if curState == 1:
                    num+=s
            elif curState == 1:
                sp=3 if s in dSet else 4
                curState=trs[curState][sp]
                num+=s
                if int(num) > INT_MAX:
                    return INT_MAX
                elif int(num) < INT_MIN:
                    return INT_MIN
            else:
                break
        return num

s=Solution()
print(s.myAtoi("words and 987"))
print(s.myAtoi("-42"))
print(s.myAtoi("42 abcd"))