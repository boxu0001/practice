'''
As part of Day 1 challenge, your manager has created a word game for you and your teammates to play.
The word game begins with your manager writing a string, and a number K on the board.
You and your teammates must find a substring of size K such that there is exactly one character that is repeated once.
In other words, there should be K - 1 distinct characters in the substring.

Write an algorithm to help your teammates find the correct answer. If no such substring can be found, return an empty list;
If multiple such substrings exit, return all of them, without repetitions. The order in which the substrings are returned does not matter.

Input: it has two arguments:

inputString: representing the string written by the manager.
num: an integer representing the number K, written by the manager on the board.

Output:

Return a list of all substrings of inputString with K characters, that have K - 1 distinct character, i.e. exactly one character is repeated,
or an empty list if no such substring exists in inputString. The order in which the substrings are returned does not matter.

Constraints:

The input integer can only be greater than or equal to 0 and less than or equal to 26 (0 <= num <= 26).
The input string consists of only lowercase alphabetic characters.

Example 1:

Input: 
inputString = awaglk
num = 4

Output:
[awag]

Explanation:
The substrings are {awag, wagl, aglk}
The answer is awag as it has 3 distinct characters in a string of size 4, and only one character is repeated twice.

Example 2:

Input: 
inputString = democracy
num = 5

Output:
[ocrac, cracy]

Example 3:

Input: 
inputString = wawaglknagagwunagkwkwagl
num = 4

Output:
[awag, naga, gagw, gkwk, wkwa]

Similar problems:

    Substrings of size K with K distinct chars
'''

from __future__ import annotations

class Solution:
    def findSubString(self, target: str, K: int ) -> list[str]:
        if K == 0:
            return []
        
        result=[]
        s=0
        e=0
        ls=len(target)
        keys={}
        while e < ls:
            if target[e] not in keys:
                keys[target[e]]=1
            else:
                keys[target[e]]+=1

            if e-s+1 == K:
                if len(keys) == K-1:
                    result+=[target[s:e+1]]
                keys[target[s]]-=1
                if keys[target[s]] == 0:
                    keys.pop(target[s])
                s+=1
            e+=1    

        return result

s=Solution()

# s.findSubString('wawaglknagagwunagkwkwagl', 4)

s.findSubString('aabb', 3)






