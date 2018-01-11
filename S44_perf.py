import math

# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).

# The matching should cover the entire input string (not partial).

# The function prototype should be:
# bool isMatch(const char *s, const char *p)

# Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "*") → true
# isMatch("aa", "a*") → true
# isMatch("ab", "?*") → true
# isMatch("aab", "c*a*b") → false

class Solution:
    def matchStr(self, s, p):
        if len(p) == len(s):
            for i in range(0, len(p)):
                if s[i] != p[i] and p[i] != '?':
                    return False
            return True
        return False        

    def isMatch(self, s, p):
        states = []
        plist = p.split('*')
        words = []

        if plist[0] != '': 
            sfirst=s[0:len(plist[0])]
            if self.matchStr(sfirst, plist[0]) == True:
                s=s[len(plist[0]):]
                plist=plist[1:]
            else:
                return False
                
        if len(plist) > 0 and plist[len(plist)-1] != '':
            lw = plist[len(plist)-1]
            slast = s[len(s)-len(lw):len(s)]    
            if self.matchStr(slast, lw) == True:
                s=s[:len(s)-len(lw)]
                plist=plist[:-1]
            else:
                return False

        containStar = '*' in p

        for wi in range(0, len(plist)):
            if plist[wi] != '': 
                words+=[plist[wi]]   

        if len(words) == 0 and containStar:  #containing only *
            return True
        elif len(words) == 0 and not containStar and len(s) > 0:    #no *
            return False
        elif len(words) == 0 and not containStar and len(s) == 0:
            return True

        tstr = s
        f = [-1]*len(tstr)
        for k in range(0, len(tstr)):
            if k>0 and f[k-1]>=0:
                if f[k-1]+1 == len(words):
                    return True
                t=k-len(words[f[k-1]+1])
                if t>=0 and f[t]==f[k-1] and f[t]+1 < len(words) and self.isMatch(tstr[t+1:k+1], words[f[t]+1]):
                    f[k] = f[k-1]+1
                else:
                    f[k] = f[k-1]                    
            else:
                t=k-len(words[0])+1
                if t>=0 and self.isMatch(tstr[t:k+1], words[0]):
                    f[k] = 0
                    

        return len(f) > 0 and f[-1]==len(words)-1 #containing last words
                
                
s = Solution()
print(s.isMatch("aaabaaabaabababbabababaababbabbbbaaaaababbaabbbaab","*babbbb*aab**b*bb*aa*"))
