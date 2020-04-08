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

The overall run time complexity should be O(log (m+n))
'''

class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArraysBrutalForce(self, A, B):
        c=sorted(A+B)
        lc = len(c)
        return (c[(lc-1)//2] + c[lc//2])/2

    def findMedianSortedArrays(self, A, B):
        la,lb = len(A), len(B)
        k1 = (la + lb -1)//2
        k2 = (la + lb)//2
        median1, median2 = None, None
        ai, bi = 0, 0
        
        while ai <= la-1 and bi <=lb -1:
            if A[ai] < B[bi]:
                anxti = self.binarySearchNextIndex(A, B[bi], ai)
                if bi + ai <= k1 <= bi + anxti:
                    median1 = A[k1 - bi]
                if bi + ai <= k2 <= bi + anxti:
                    median2 = A[k2 - bi]
                ai = anxti + 1 
            else:
                bnxti = self.binarySearchNextIndex(B, A[ai], bi)
                if ai + bi <= k1 <= ai + bnxti:
                    median1 = B[k1 - ai]
                if ai + bi <= k2 <= ai + bnxti:
                    median2 = B[k2 - ai]
                bi = bnxti + 1

            if median1 != None and median2 != None:
                break

        if median1 == None:
            median1 = B[k1-la] if ai == la else A[k1-lb]
        if median2 == None:
            median2 = B[k2-la] if ai == la else A[k2-lb]

        return (median1 + median2) / 2
    
    # find C[r] <= target < C[r+1] or END, return r, assume C[0] <= target
    def binarySearchNextIndex(self, C, target, start):
        end = len(C) -1
        si, ei = start, end
        r = None
        while si < ei:
            mi = (si+ei)//2
            if C[mi] <= target < C[mi+1]:
                r = mi
                break
            elif C[mi] > target:
                ei = mi     #important, not ei = mi -1
            else:
                si = mi + 1
        # if not found or start == end
        if r == None:
            r = end
        return r

s=Solution()
s.findMedianSortedArrays([1,2,3,4,5,6], [2,3,4,5])