from __future__ import annotations
import heapq as pq

class Solution:
    # N =len(arr) , K find Kth largest element
    def findKthLargestInArrayWithGrowingD(self, N: int, arr: list[int], K: int) -> int:
        
        Y=[]
        Z=arr
        occurs=set(arr)
        kq=[]

        for i in arr:
            if len(kq) < K:
                pq.heappush(kq, i)
            elif kq[0] < i:
                pq.heapreplace(kq, i)
            else:
                pass

        while Z:    
            Z_new=[]
            for i in range(len(Z)):
                for j in range(i+1, len(Z)):
                    d=abs(Z[i]-Z[j])
                    if d not in occurs:
                        occurs.add(d)
                        Z_new+=[d] 
                        if len(kq) < K:
                            pq.heappush(kq, d)
                        elif kq[0] < d:
                            pq.heapreplace(kq, d)
                        else:
                            pass

            for i in range(len(Y)):
                for j in range(len(Z)):
                    d = abs(Y[i]-Z[j])
                    if d not in occurs:
                        occurs.add(d)
                        Z_new+=[d]
                        if len(kq) < K:
                            pq.heappush(kq, d)
                        elif kq[0] < d:
                            pq.heapreplace(kq, d)
                        else:
                            pass
        
            Y=Y+Z
            Z=Z_new
        

        res = -1
        if len(kq) == K > 0:
            res = kq[0]

        return res


s=Solution()
# s.findKthLargestInArrayWithGrowingD(5, [1,3,5,6,7], 2) # expect 6
# s.findKthLargestInArrayWithGrowingD(1, [1], 2) #expect -1
s.findKthLargestInArrayWithGrowingD(3, [90, 82], 3) #expect 86

