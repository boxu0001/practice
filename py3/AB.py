# You are given two s: N and K. Lun the dog is interested in strings that satisfy the following conditions:

#     The string has exactly N characters, each of which is either 'A' or 'B'.
#     The string s has exactly K pairs (i, j) (0 <= i < j <= N-1) such that s[i] = 'A' and s[j] = 'B'.

# If there exists a string that satisfies the conditions, find and return any such string. Otherwise, return an empty string.

# Limits
# Time limit (s):
# 2.000
# Memory limit (MB):
# 256
# Constraints
# - N will be between 2 and 50, inclusive.
# - K will be between 0 and N(N-1)/2, inclusive.
# Examples
# 0)
# 3
# 2
# Returns: "ABB"
# This string has exactly two pairs (i, j) mentioned in the statement: (0, 1) and (0, 2).
# 1)
# 2
# 0
# Returns: "BA"
# Please note that there are valid test cases with K = 0.
# 2)
# 5
# 8
# Returns: ""
# Five characters is too short for this value of K.
# 3)
# 10
# 12
# Returns: "BAABBABAAB"
# Please note that this is an example of a solution; other valid solutions will also be accepted.
import math
class AB:
    def createString(self, N, K):
        bstack = []
        if N*N < 4*K:
            return ""
            
        # minB = math.ceil((N - math.sqrt(N*N-4*K))/2)
        # maxB = math.floor((N + math.sqrt(N*N-4*K))/2)
        b = N//2    #number of B
        a = K//b    #number of A without first A
        c = K%b     #first A's postion, AB...B, (c X B), or no A if 0

        baseStr = 'A'*a + ('B'*b if c==0 else 'B'*(b-c) + 'A' + 'B'*c)
        result = baseStr 
        if len(baseStr) < N:
            result = 'B'*(N-len(baseStr)) + baseStr

        return result

k=AB()
print(k.createString(5,8))
print(k.createString(10,12))
