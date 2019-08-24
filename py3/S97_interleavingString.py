# 97. Interleaving String
# Hard

# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

# Example 1:

# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true

# Example 2:

# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1=len(s1)
        len2=len(s2)
        len3=len(s3)
        if len1+len2 != len3:
            return False
        bfsQueue=[(0,0)]
        while bfsQueue:
            li, lj=bfsQueue.pop(0)
            if len3==li+lj:
                return True
            else:
                if li < len1 and s1[li] == s3[li+lj]:
                    bfsQueue+=[(li+1, lj)]
                if lj < len2 and s2[lj] == s3[li+lj]:
                    if bfsQueue and (bfsQueue[-1] == (li, lj+1)):   #the condition used with BFS to reduce the duplicates, important!
                        #duplicate
                        pass
                    else:
                        bfsQueue+=[(li, lj+1)]
        return False
            
#1. use BFS queue to handle the split of n: (0,n), (1, n-1)...(n,0)
#2. the problem can be worked out by s3[0:n] := {s1[0:i] ~ s2[0:j] where i,j are fitting the interleaving}
#then s3[0:n+1] := {s1[0:i+1]~s2[0:j] or s1[0:i]~s2[0:j+1] if fitting}
#using YangHui triangle to illustrate:
#               (0,0)
#         (1,0)       (0,1)
#     (2,0)     (1,1)       (0,2)
# (3,0)   (2,1)       (1,2)       (0,3)
# ...



#there is a DP solution as well