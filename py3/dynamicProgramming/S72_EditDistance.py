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
        if l1 == 0 and l2 == 0:
            return 0
        elif l1 == 0:
            return l2
        elif l2 == 0:
            return l1

        f = [[0 for j in range(l2)] for i in range(l1)] 
        for i in range(l1):
            for j in range(l2):
                if word1[i] == word2[j]:
                    f[i][j] = f[i-1][j-1] + 1 if i >= 1 and j >= 1 else 1
                else:
                    f[i][j] = max(0 if i-1 < 0 else f[i-1][j], 0 if j-1 < 0 else f[i][j-1])
        
        countDown = 0
        countLeft = 0
        count = 0
        i = l1-1
        j = l2-1
        while i>0 or j>0:
            if word1[i] == word2[j]:
                i= 0 if i == 0 else i-1
                j= 0 if j == 0 else j-1
                count+=max(countDown, countLeft)
                countDown = 0
                countLeft = 0
            elif i > 0 and f[i][j] == f[i-1][j]:
                i -= 1
                countLeft+=1
            else:
                j -= 1
                countDown+=1

        count+= max(countDown, countLeft) + 1 - f[0][0]
        return count

s = Solution()         
print(s.minDistance("ab", "ba"))
print(s.minDistance("intention", "execution"))
print(s.minDistance("horse", "ros"))
print(s.minDistance("mart", "karma"))




