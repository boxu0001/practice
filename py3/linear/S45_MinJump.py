# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.
# For example:
# Given array A = [2,3,1,1,4]

# The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

# Note:
# You can assume that you can always reach the last index.

class Solution:
    def jump(self, nums):
        # f(e) = minium steps from 0 to element
        # find f(len(nums)-1)
        ln = len(nums)
        step = 1
        lf=0
        rt=0
        maxi=0
        while(lf <= rt and lf < ln-1):
            ci=lf+nums[lf]
            maxi = ci if ci > maxi else maxi
            if maxi >= ln-1:
                return step
            if lf==rt:
                step+=1
                if maxi > rt:                
                    lf=rt+1
                    rt=maxi
                else:
                    return 0
            else:
                lf+=1
        return 0

s = Solution()
print(s.jump([2,3,1,1,4]))
print(s.jump([0]))
print(s.jump([1,1,1,1]))
print(s.jump([1]))