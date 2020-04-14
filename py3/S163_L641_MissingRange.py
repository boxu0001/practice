'''
Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.
Have you met this question in a real interview?  
Example

Example 1

Input:
nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99
Output:
["2", "4->49", "51->74", "76->99"]
Explanation:
in range[0,99],the missing range includes:range[2,2],range[4,49],range[51,74] and range[76,99]

Example 2

Input:
nums = [0, 1, 2, 3, 7], lower = 0 and upper = 7
Output:
["4->6"]
Explanation:
in range[0,7],the missing range include range[4,6]
'''


class Solution:
    """
    @param: nums: a sorted integer array
    @param: lower: An integer
    @param: upper: An integer
    @return: a list of its missing ranges
    """
    def findMissingRanges(self, nums, lower, upper):
        # write your code here
        r=[]
        prev = lower
        nums+=[upper+1]
        for cur in nums:
            if cur - prev >= 2:
                r += [str(prev) + '->' + str(cur-1)]
            elif cur - prev == 1:
                r += [str(cur-1)]
            prev = cur + 1
        return r

