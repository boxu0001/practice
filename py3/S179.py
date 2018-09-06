# Given a list of non negative integers, arrange them such that they form the largest number.
# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
# Note: The result may be very large, so you need to return a string instead of an integer.

class Solution:
    def largestNumber(self, nums):
        
        a=[]
        sr=[i for i in range(0, len(nums))]
        k=0
        for i in nums:
            sn=str(i)
            a+=[[int(ai) for ai in sn]]
            if len(sn) > k:k=len(sn)
        k=k*2            
        while(k>0):
            k-=1
            b=[0]*11
            for j in sr:
                laj=len(a[j])
                curDigit=a[j][k if k<laj else k%laj] 
                b[curDigit+1]+=1
            for bx in range(1, 10): b[bx]+=b[bx-1]
            srn=[0]*len(nums)    
            for j in sr:
                laj=len(a[j])
                curDigit=a[j][k if k<laj else k%laj]
                srn[b[curDigit]]=j
                b[curDigit]+=1
            sr=srn  
        rt= '0' if nums[sr[-1]] == 0 else "".join(str(nums[i]) for i in sr[::-1])
        return rt

s=Solution()
# print(s.largestNumber([3, 30, 34, 5, 9876]))
# nums=
# nums=
nums=[12,121]
print(s.largestNumber(nums))
print(s.largestNumber([3, 30, 34, 5, 9876]))
print(s.largestNumber([57, 56, 0, 29 ]))
print(s.largestNumber([0, 0, 0, 0 ]))