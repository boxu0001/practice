
class Solution(object):
    def findSubstring(self, s, words):
        rtype=[]        
        wordCount={}
        for w in words:
            if wordCount.has_key(w):
                wordCount[w]+=1
            else:
                wordCount[w]=1

        wl=len(words[0])
        lenSubStr=wl*len(words)
        lastTryPos = 0
        if len(s) < lenSubStr:
            return rtype
        else:
            lastTryPos=len(s)-lenSubStr+1

        for j in range(0, wl):
            queueJ=j
            nextJ=j  
            cacheWordCnt={}
            while (True):
                nextTwd=s[nextJ:nextJ+wl]
                if nextTwd in wordCount and nextTwd in cacheWordCnt and wordCount[nextTwd] > cacheWordCnt[nextTwd]:
                    cacheWordCnt[nextTwd]+=1
                    nextJ=nextJ+wl
                    if nextJ-queueJ == lenSubStr:
                        rtype+=[queueJ]
                elif nextTwd in wordCount and nextTwd not in cacheWordCnt:
                    cacheWordCnt[nextTwd]=1
                    nextJ=nextJ+wl
                    if nextJ-queueJ == lenSubStr:
                        rtype+=[queueJ]
                else:
                    if queueJ < nextJ:
                        topWd=s[queueJ:queueJ+wl]
                        if topWd in cacheWordCnt and cacheWordCnt[topWd] > 0:
                            cacheWordCnt[topWd]-=1
                        queueJ=queueJ+wl                            
                    else:
                        nextJ=nextJ+wl
                        queueJ=nextJ                 

                if nextJ >= len(s):
                    break;

        return rtype

    def firstMissingPositive(self, nums):
        m=len(nums)
        t={}
        for ni in nums:
            if 0< ni <= m:
                t[ni]=1
        
        lt=len(t)
        for ti in range(1, lt+1):
            if not t.has_key(ti):
                return ti
        
        return lt+1
        

s=Solution()
print s.findSubstring("barfoothefoobarman",["bar",'foo'])