# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
class solution:
    def sum2(self, nums:list, target):
        ni=[(i, n) for i, n in enumerate(nums)]
        ni.sort(key=lambda k : k[1])
        s,e=0, len(ni)-1
        while s < e:
            if ni[s][1] + ni[e][1] < target:
                s+=1
            elif ni[s][1] + ni[e][1] > target:
                e-=1
            else:
                return [ni[s][0], ni[e][0]]


s=solution()
print(s.sum2([11, 15, 2, 7], 9))
