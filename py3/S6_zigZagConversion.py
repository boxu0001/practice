#The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR". 

class Solution:
    def convert(self, s, nr):
        # 0 - 0*2(nr-1) , 1*2(nr-1),  2*2(nr-1)
        # 1 - 0*2(nr-1)+1,  2nr-1-1, 1*2(nr-1)+1 , 2*(2nr-1) -1
        # 2 - 0*2(nr-1)+2,  2nr-1-2, 1*2(nr-1)+2 , 2*(2nr-1) -2
        # ..
        # nr-1 - nr-1, 1*2(nr-1)+nr-1

        if nr <= 1:
            return s
        rtype=[]
        for i in range(0,nr,1):
            for t in range(i, len(s), nr*2-2):
                rtype+=[s[t]]
                if 0<i<nr-1 and t-i+2*nr-2-i < len(s):
                    rtype+=[s[t-2*i+2*nr-2]]            # t - 2nr-1 - (2i-1)    -> 2nr-1 为一个循环，减去 上部多出的 2i-1
        return "".join(rtype)
s=Solution()
print(s.convert("PAYPALISHIRING", 3))
print(s.convert("", 3))

