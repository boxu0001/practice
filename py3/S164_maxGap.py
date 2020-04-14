'''
164. Maximum Gap
Hard

Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Return 0 if the array contains less than 2 elements.

Example 1:

Input: [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either
             (3,6) or (6,9) has the maximum difference 3.

Example 2:

Input: [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
'''
from __future__ import annotations
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        ls = len(nums)
        if ls <= 1:
            return 0
            
        ms = min(nums)
        mx = max(nums)
        #divide the length by (ls-1), each spans "span" length
        # maxium by Pigeon Hole: ms + span*(ls-1) -1 < mx, so there must be value > span
        span = max(1, (mx - ms) // (ls-1))  
        numOfBuckets = (mx - ms) // span + 1
        buckets = [[None,None]] * numOfBuckets
        for n in nums:
            i = (n-ms+1)//span
            msi, mxi = buckets[i]
            if msi:
                buckets[i] = [min(msi, n), max(mxi, n)]
            else:
                buckets[i] = [n, n]
        r = 0
        _, prvMax = buckets[0]
        for i in range(1, len(buckets)):
            curMin, curMax = buckets[i]
            if curMin:
                r = max(r, curMin - prvMax)
                prvMax = curMax
        return r
# 如果用radix sort的话， 空间消耗会很大, O(数值的范围) = O(1<<32), 不推荐
# 这里用到抽屉原理， 让最大的GAP（求的结果）大于抽屉的容量， 这样就不需要考虑抽屉内部的比较，只需比较抽屉与抽屉之间的GAP
# range=抽屉的容量, numOfBuckets=抽屉的个数， m = minimu, n = max, ls = length of the nums
#       m + range * (ls-1) -1 < n ===> range < (n-m+1)/(ls-1) ===> range = (n-m)//(ls-1) < (n-m+1)/(ls-1), 
#       numOfBuckets = (mx - ms) // span + 1
# 注意，range of 6~9 inclusive counting 是 4, 包含的个数
# 将数 hash 到 抽屉上， O(ls), 遍历抽屉 O(ls), time complexity O(ls), space complexity O(ls)
# 

s=Solution()
# s.maximumGap([2,5,7,10])
s.maximumGap([1,4,8,11,14,19])