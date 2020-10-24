'''
216. Combination Sum III
Medium

Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

    Only numbers 1 through 9 are used.
    Each number is used at most once.

Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

 

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.

Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.

Example 3:

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations. [1,2,1] is not valid because 1 is used twice.

Example 4:

Input: k = 3, n = 2
Output: []
Explanation: There are no valid combinations.

Example 5:

Input: k = 9, n = 45
Output: [[1,2,3,4,5,6,7,8,9]]
Explanation:
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45
​​​​​​​There are no other valid combinations.

 

Constraints:

    2 <= k <= 9
    1 <= n <= 60

'''
from __future__ import annotations
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result=[[0]]
        
        for i in range(k):
            tmp=[]
            for xlist in result:                
                total = xlist[0]
                start = xlist[-1]
                if n-total > (20-(k-i))*(k-i)//2:
                    continue
                if (start*2+k-i+1)*(k-i)//2 > n-total:
                    continue
                
                for j in range(start+1, 10):
                    if j+total <= n:
                        nl = xlist+[j]
                        nl[0] += j
                        tmp+=[nl]
                    else:
                        break
            result=tmp
        
        return [ x[1:] for x in result if x[0] == n ]
   
        
s=Solution()
s.combinationSum3(3,7)

