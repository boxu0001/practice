class Solution:
    # problem 44
    
    def isMatch(self, s, p):
        ls=len(s)
        lp=len(p)
        mt=[]
        for pi in range(0, lp+1):
            for si in range(0, ls+1):
                if pi == 0 and si == 0:
                    mt+=[[True]]
                elif pi == 0 and si > 0:
                    mt[0]+=[False]
                elif pi > 0 and si == 0:
                    mt+=[[True if p[pi-1] == "*" and mt[pi-1][0] else False]]
                elif p[pi-1] != "*":
                    mt[pi] += [mt[pi-1][si-1] and (p[pi-1] == s[si-1] or p[pi-1] == "?")]
                else:
                    mt[pi]+=[mt[pi][si-1] or mt[pi-1][si]]
        # print(mt)                    
        return mt[lp][ls]



s = Solution()
print(s.isMatch("aaabaaabaabababbabababaababbabbbbaaaaababbaabbbaab","*babbbb*aab**b*bb*aa*"))    
print(s.isMatch("bad","*"))    
print(s.isMatch("a","*a")) 
print(s.isMatch("a","a*"))
print(s.isMatch("ab","*a")) 
print(s.isMatch("ab","a*"))