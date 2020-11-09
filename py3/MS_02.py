
from __future__ import annotations

class Solution:
    def patternRec(self, input: str) -> str:
        semiIdx = input.index(';')
        pattern =input[:semiIdx]
        targets = input[semiIdx+1:].split('|')
        res=[0]*len(targets)
        
        for i, target in enumerate(targets):
            if pattern == '':
                if target == '':
                    res[i]+=1
                continue
            for j in range(len(target)):
                if target[j:].startswith(pattern):
                    res[i]+=1
        
        s =sum(res)
        res+=[s]
        return '|'.join(str(n) for n in res)

s=Solution()
# print(s.patternRec('bc;bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32'))
print(s.patternRec(';bcdefbcbebc||cbdbesfbcy|1bcdef23423bc32'))



