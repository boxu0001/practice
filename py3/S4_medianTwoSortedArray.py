'''
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays.
Have you met this question in a real interview?  
Clarification

    The definition of the median:

    The median here is equivalent to the median in the mathematical definition.

    The median is the middle of the sorted array.

    If there are n numbers in the array and n is an odd number, the median is A[(n-1)/2].

    If there are n numbers in the array and n is even, the median is (A[n / 2] + A[n / 2 + 1]) / 2.

    For example, the median of the array A=[1,2,3] is 2, and the median of the array A=[1,19] is 10.

Example

Example 1

Input:
A = [1,2,3,4,5,6]
B = [2,3,4,5]
Output: 3.5

Example 2

Input:
A = [1,2,3]
B = [4,5]
Output: 3

Challenge

The overall run time complexity should be O(log (m+n)).
'''

class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, nums1, nums2):
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
                    return (m[i] + n[j-1])/2 if endIndex < 0 else (m[i-1] + n[j])/2
                elif startIndex >= lm:
                    return (max(n[j-1],m[i-1]) + n[j])/2 if even else n[j]
                else:
                    return (n[j-1] + n[j])/2 if even else n[j]                    
            i=(startIndex+endIndex)//2              
            j=halfCount-i                           
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

s=Solution()
s.findMedianSortedArrays([1,2,3,4,5,6],[2,3,4,5])
