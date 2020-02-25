'''
151. Reverse Words in a String
Medium

Given an input string, reverse the string word by word.

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"

Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        result = None
        stack=[[]]
        for si in s:
            top = stack[-1]
            if si == " " and len(top) != 0:
                stack+=[[]]
            elif si != " ":
                top+=[si]
            else:
                pass
        result = " ".join("".join(ss) for ss in stack[::-1] if len(ss) > 0)
        return result

    def reverseWords2(self, s: str) -> str:
        a=s.split(" ")
        return " ".join(x for x in a[::-1] if x != "")

s = Solution()
print(s.reverseWords2("  hello world!  "))
    
