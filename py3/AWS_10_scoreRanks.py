
from __future__ import annotations
class Solution:
    #return number of players able to level up
    def getNumOfPassed(self, cutoffRank: int, num: int, scores: list[int]) -> int:
        scores = sorted(scores)
        curScore=-1
        curNumber=1
        curRank=0
        result=0
        for sc in scores[::-1]:
            if sc == curScore:
                curNumber+=1
            else:
                curScore = sc
                curRank += curNumber
                curNumber=1
            
            if curRank <= cutoffRank and sc > 0:
                result+=1
            else:
                break

        return result


s=Solution()
# s.getNumOfPassed(3, 4, [100,50,50, 25])

s.getNumOfPassed(4, 7, [1,2,2,3,3,5,5])