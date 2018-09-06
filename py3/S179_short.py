from functools import cmp_to_key
class Solution:

    def largestNumber(self, nums):                
        numstr=[str(i) for i in nums]
        ss=sorted(numstr, key=cmp_to_key(lambda x,y: 1 if x+y>y+x else -1 if x+y<y+x else 0), reverse=True)
        return '0' if int(ss[0]) == 0 else "".join(ss)

s=Solution()
# print(s.largestNumber([3, 30, 34, 5, 9876]))
# nums=
# nums=
# nums=[12,121]
# print(s.largestNumber(nums))
# print(s.largestNumber([3, 30, 34, 5, 9876]))
print(s.largestNumber([57, 56, 0, 29 ]))
print(s.largestNumber([1,2]))