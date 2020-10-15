'''
1375. Substring With At Least K Distinct Characters

Description

Given a string S with only lowercase characters.

Return the number of substrings that contains at least k distinct characters.

    10 ≤ length(S) ≤ 1,000,000
    1 ≤ k ≤ 26

Have you met this question in a real interview?  
Example

Example 1:

Input: S = "abcabcabca", k = 4
Output: 0
Explanation: There are only three distinct characters in the string.

Example 2:

Input: S = "abcabcabcabc", k = 3
Output: 55
Explanation: Any substring whose length is not smaller than 3 contains a, b, c.
    For example, there are 10 substrings whose length are 3, "abc", "bca", "cab" ... "abc"
    There are 9 substrings whose length are 4, "abca", "bcab", "cabc" ... "cabc"
    ...
    There is 1 substring whose length is 12, "abcabcabcabc"
    So the answer is 1 + 2 + ... + 10 = 55.
'''

class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: the number of substrings there are that contain at least k distinct characters
    """
    def kDistinctCharacters(self, s, k):
        # Write your code here
        lens = len(s)
        count = 0
        
        sipre=-1 #previous shortest substring start index
        si=0    # a substring start index
        ei=0    # a substring end index
        cache={}
        while si <= ei:
            if len(cache.keys()) < k and ei < lens:
                if s[ei] not in cache:
                    cache[s[ei]] = 1
                else:
                    cache[s[ei]] += 1
                ei+=1
            elif len(cache.keys()) == k:
                # just k distincts
                cache[s[si]]-=1
                if cache[s[si]] == 0:   #find a shortest substring
                    cache.pop(s[si])
                    count+=(si-sipre)*(lens-ei+1)   # Note: ei has been +1, ei-1 is the end index
                    sipre = si
                si+=1
            else:
                break
        
        return count    
                
            
s=Solution()
s.kDistinctCharacters('abcabcabcabc', 3)
