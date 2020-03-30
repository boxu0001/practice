'''
640. One Edit Distance

Given two strings S and T, determine if they are both one edit distance apart.
One ediit distance means doing one of these operation:

    insert one character in any position of S
    delete one character in S
    change one character in S to other character

Example

Example 1:

Input: s = "aDb", t = "adb" 
Output: true

Example 2:

Input: s = "ab", t = "ab" 
Output: false
Explanation:
s=t ,so they aren't one edit distance apart
'''

class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if they are both one edit distance apart or false
    """
    def isOneEditDistance(self, s, t):
        # write your code here
        lens = len(s)
        lent = len(t)
        if lens == lent:
            cnt = 0
            for i in range(lens):
                if s[i] != t[i]:
                    cnt += 1
                if cnt > 1:
                    return False
            if cnt == 1:
                return True
            else:
                return False
        elif lens == lent + 1 or lent == lens + 1:
            if lens < lent:
                m, n, lm, ln = s, t, lens, lent  
            else: 
                m, n, lm, ln = t, s, lent, lens
            i = 0
            j = 0
            while i < lm and j < ln:
                if m[i] == n[j]:
                    i += 1
                j += 1
                if j - i > 1:
                    return False
            return True
        else:
            return False
