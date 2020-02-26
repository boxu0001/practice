'''
The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

The read function may be called multiple times.
Have you met this question in a real interview?  
Example

Example 1

Input:
"filetestbuffer"
read(6)
read(5)
read(4)
read(3)
read(2)
read(1)
read(10)
Output:
6, buf = "filete"
5, buf = "stbuf"
3, buf = "fer"
0, buf = ""
0, buf = ""
0, buf = ""
0, buf = ""

Example 2

Input:
"abcdef"
read(1)
read(5)
Output:
1, buf = "a"
5, buf = "bcdef"
'''

"""
The read4 API is already defined for you.
@param buf a list of characters
@return an integer
you can call Reader.read4(buf)
"""

class Solution:

    def __init__(self) :
        self.head = 0
        self.tail = 0
        self.lastBuf = [None for _ in range(4)]

    # @param {char[]} buf destination buffer
    # @param {int} n maximum number of characters to read
    # @return {int} the number of characters read
    def read(self, buf, n):
        # Write your code here
        cnt = 0
        i = 0
        while cnt < n:
            if self.tail == self.head:
                i = Reader.read4(self.lastBuf)
                self.head = 0
                self.tail = i
                if i == 0:
                    break
            while self.head < self.tail and cnt < n:
                buf[i] = self.buffer[self.head]
                i+=1
                self.head+=1
                cnt+=1
        return cnt

