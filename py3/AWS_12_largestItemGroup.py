
from __future__ import annotations
class Solution:
    def largestItemAssociation(self,  itemAssociation: list[list[str]] ) -> list[str] :
        
        matrix={}
        for [A, B] in itemAssociation:
            if A not in matrix:
                matrix[A] = {B}
            else:
                matrix[A].add(B)
            
            if B not in matrix:
                matrix[B] = {A}
            else:
                matrix[B].add(A)
        
        result=[]
        sortedItems = sorted(matrix.keys())     # Nlog(K)
        for item in sortedItems:                
            if item in matrix:
                temp=[]
                queue=[item]                    
                while queue:                    # K
                    curItem = queue.pop(0)      # queue max length is K
                    temp+=[curItem]
                    if curItem in matrix:
                        nxtset = matrix.pop(curItem)    # K
                        for nxitm in nxtset:
                            if nxitm in matrix and nxitm not in queue: # 1
                                queue+=[nxitm]

                if len(temp) > len(result) or (len(temp) == len(result) and  temp[0] < result[0]):
                    result = temp
                
        return result


s=Solution()
s.largestItemAssociation([["I1", "I2"], ["I3", "I4"], ["I4", "I5"], ["I2", "I6"]])