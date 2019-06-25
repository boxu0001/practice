# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 

# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occ={}                  #map contains {character, index} 存当前窗口所有 字符--索引 
        si=0                    #窗口开始索引
        result=0
        for ei in range(len(s)):    #ei 是当前探索索引， 一步步向右探索
            cc = s[ei]              #cc 是当前字符
            if cc in occ:           #如果cc和当前窗口某个字符中，（注意，这一步的目的是保持窗口里字符的不重复性）
                for removed in range(si, occ[cc]):  #把所有重复字符索引之前 都清除，
                    occ.pop(s[removed])
                si=occ.pop(cc) + 1                  #把重复字符清除 并把窗口开始索引重设为 重复字符索引的下一个
            lse = ei-si+1
            if lse > result:
                result = lse
            occ[cc]=ei
        return result
                
s=Solution()
print(s.lengthOfLongestSubstring("tmmzuxt"))
print(s.lengthOfLongestSubstring("aab"))