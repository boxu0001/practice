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
            i = (n-ms)//span
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
        