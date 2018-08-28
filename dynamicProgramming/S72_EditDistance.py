# Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

# You have the following 3 operations permitted on a word:

#     Insert a character
#     Delete a character
#     Replace a character

# Example 1:

# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')

# Example 2:

# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 = len(word1)
        l2 = len(word2)
        if l1 == 0:
            return l2
        elif l2 == 0:
            return l1
        f = [[0 for j in range(l2)] for i in range(l1)] 
        for i in range(l1):
            for j in range(l2):
                if word1[i] == word2[j]:
                    f[i][j] = j if i==0 else i if j==0 else f[i-1][j-1]
                else:
                    p = min(j if i == 0 else f[i-1][j], i if j == 0 else f[i][j-1])
                    if i > 0 and j > 0 and p > f[i-1][j-1]:
                        p = f[i-1][j-1]
                    f[i][j] = p+1
        return f[-1][-1]

    def minDistance2(self, A, B):
        l1 = len(A)+1
        l2 = len(B)+1
        f = [[None for j in range(l2)] for i in range(l1)] 
        for i in range(l2):
            f[0][i] = i
        for j in range(l1):
            f[j][0] = j            
        for i in range(1, l1):
            for j in range(1, l2):
                f[i][j] = f[i-1][j-1] if A[i-1] == B[j-1] else (min(f[i-1][j], f[i][j-1], f[i-1][j-1]) + 1)
        return f[-1][-1]

s = Solution()         
print(s.minDistance2("", ""))
print(s.minDistance2("", "ab"))
print(s.minDistance2("ab", "ba"))
print(s.minDistance2("intention", "execution"))
print(s.minDistance2("horse", "ros"))
print(s.minDistance2("mart", "karma"))



