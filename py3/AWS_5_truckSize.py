

from __future__ import annotations
class Solution:
    def getMaxUnit(self, num: int, boxes: list[int], unitSize: int, unitsPerBox: list[int], truckSize: int) -> int:
        
        #sort unitsPerBox
        unitsBoxs = [[unitsPerBox[i], boxes[i]] for i in range(num)]
        unitsBoxs = sorted(unitsBoxs)

        result=0
        for [ux, bx] in unitsBoxs[::-1]:
            if truckSize >= bx:
                result+=ux*bx
                truckSize -= bx
            elif bx > truckSize > 0:
                result+=ux*truckSize
                truckSize =0
            else:
                break
        return result

s=Solution()

# s.getMaxUnit(5, [2,3,3,1,2], 3, [1,1,2,3,1], 4)
s.getMaxUnit(1, [3], 1, [2], 1)




