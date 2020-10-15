# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# You may assume nums1 and nums2 cannot be both empty.

# Example 1:

# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0

# Example 2:

# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        c1=len(nums1)
        c2=len(nums2)
        even=True if (c1+c2)%2 == 0 else False
        half=(c1+c2-2)//2+1 #cover both even/odd number
        m,n = (nums1, nums2) if c1 < c2 else (nums2,nums1)
        if len(m) == 0:
            return (n[half-1] + n[half])/2 if even else n[half]
        sti, edi = 0, len(m)-1
        while(True):  #not cover empty case
            i=(sti+edi)//2 if sti <= edi else edi+1
            j=half-i
            mi1 = m[i-1] if i > 0 else n[j-1]
            mi = m[i] if i < len(m) else n[j]
            nj1 = n[j-1] if j > 0 else m[i-1]
            nj = n[j] if j < len(n) else m[i]
            if (mi >= nj1 and nj >= mi1) or edi < sti:
                return (max(mi1,nj1) + min(mi,nj))/2 if even else min(mi,nj)
            elif mi1 > nj and i > 0:
                edi = i-1
            else:
                sti = i+1
        return (max(mi1,nj1) + min(mi,nj))/2 if even else min(mi,nj)

    def findMedianSortedArrays2(self, nums1, nums2):
        m,n = (nums1, nums2) if len(nums1) < len(nums2) else (nums2,nums1)
        lm=len(m)
        ln=len(n)
        even=(lm+ln)%2==0
        startIndex = 0
        endIndex = lm-1
        halfCount=(lm+ln-2)//2+1
        if lm == 0:
            j=halfCount
            return (n[j-1] + n[j])/2 if even else n[j]
        while True:
            if endIndex < 0 or startIndex >= lm:
                i = halfCount - lm if endIndex < 0 else lm # i=0, else i=lm
                j = halfCount - i  
                if lm == ln:
                    #if startIndex >= lm,  i-1=-1 is the last m small element, use (n[0] + m[-1])/2
                    #if endIndex < 0, j-1=-1 is the last n small element, use (m[0] + n[-1])/2
                    return (m[i] + n[j-1])/2 if endIndex < 0 else (m[i-1] + n[j])/2
                elif startIndex >= lm:
                    return (max(n[j-1],m[i-1]) + n[j])/2 if even else n[j]
                else:
                    i=0
                    j=halfCount-i
                    return (n[j-1] + n[j])/2 if even else n[j]                    
            i=(startIndex+endIndex)//2              # "i" is the start index of the greater number set on m
            j=halfCount-i                           # "j" is the start index of the greater number set on n
            if (m[i] >= n[j-1]) and (i==0 or n[j] >= m[i-1]):
                if i == 0 and lm == ln:
                    return (n[j-1]+m[i])/2
                elif i == 0:
                    return (n[j-1]+min(m[i],n[j]))/2 if even else min(m[i],n[j])
                else:
                    return (max(m[i-1],n[j-1])+min(m[i],n[j]))/2 if even else min(m[i],n[j])
            elif m[i] < n[j-1]:
                startIndex = i+1
            else:
                endIndex = i-1          


    def findkthElementOfTwoSortedArray(self, K, nums1, nums2):
        N1 = len(nums1)
        N2 = len(nums2)

        if not nums2 or (K < N1 and nums1 and nums2[0] >= nums1[K]):
            return nums1[K]
        
        if not nums1 or (K < N2 and nums2 and nums1[0] >= nums2[K]):
            return nums2[K]
        
        # K < N1 + N2
        k1 = min(K, N1-1)
        k2 = K-k1

        while True:
            if 0 <= k1:
                if k2 < 0 or k2 == N2 or (k2 > 0 and nums2[k2-1] <= nums1[k1] <= nums2[k2]) or (k2==0 and nums1[k1] <= nums2[k2]):
                    return nums1[k1] 
                elif nums1[k1] > nums2[k2]: #N2 > k2 >=0 
                    if k1 == 0:
                        return nums2[k2]
                    else:
                        delta = min(N2-k2, k1 - k1//2)  
                        k1 -= delta 
                        k2 += delta #k2 can be N2, which means the entire nums2 is smaller than k1
                    
                else: # nums1[k1] < nums2[k2-1] <= nums[k2], k2 must > 0
                    N2, N1, k2, k1, nums2, nums1 = N1, N2, k1, k2, nums1, nums2

            else: # k1 < 0
                return nums2[k2]

    def findMedianSortedArrays3(self, nums1, nums2):
        N1 = len(nums1)
        N2 = len(nums2)
        m1 = (N1+N2-1)//2
        m2 = (N1+N2)//2
        med1 = self.findkthElementOfTwoSortedArray(m1, nums1, nums2)
        if m2 == m1:
            return med1
        med2 = self.findkthElementOfTwoSortedArray(m2, nums1, nums2)
        return (med1+med2)/2




s=Solution()
# print(s.findMedianSortedArrays([1,2],[-1,3]))
# print(s.findMedianSortedArrays([1,5],[2,2]))

# print(s.findMedianSortedArrays2([1],[-1,3]))
print(s.findMedianSortedArrays3([10002, 10005],[10000]))
print(s.findMedianSortedArrays3([1],[2, 3, 4]))

# s.findkthElementOfTwoSortedArray(1, [10002, 10005],[10000])


