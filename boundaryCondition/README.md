The general approach is to find the basic solution, then fit boundary conditions into basic solution.

Example: Medium of Two Sorted Array
Basic solution is to use binary search to find medium.
Start from two array m, n, with len(m) <= len(n), using binary searching as approach

```    
even=(len(m)+len(n))%2==0
startIndex = 0
endIndex = len(m)-1
halfCount = ?                               #halfCount is the count of smaller number set
while True:
    i=(startIndex+endIndex)//2              # "i" is the start index of the greater number set on m
    j=halfCount-i                           # "j" is the start index of the greater number set on n
    if m[i] >= n[j-1] and n[j] >= m[i-1]:
        return (max(m[i-1],n[j-1])+min(m[i],n[j]))/2 if even else min(m[i],n[j])
    else if m[i] < n[j-1]:
        startIndex = i+1    #using right half to increase m[i]
    else:
        endIndex = i-1    #using left half to decrease m[i]
```

However the intuitive conditions are:
A. even vs odd length.

B. empty m vs non-empty m.

C. i==-1, in which case j=halfCount-i > halfCount, both i and j can be overflow (such as m=[100] and too big).

D. i==0, in which case j=halfCount and if len(m) = len(n), can cause j over flow.

E. i==len(m), in which case, eg m=[-100] and to small, both i and j can be overflow.


Case A:
We use following
    
```
    halfCount=(len(m)+len(n)-2)//2+1
```

Case B:
We use following before while loop
    
```
    if len(m) == 0:
        j=halfCount
        return n[j] if odd else (n[j-1] + n[j])/2
```

Case C, Case D, Case E:
What about redesign with:
    
```
    if (i>=len(m) or m[i] >= n[j-1]) and (i<=0 or n[j] >= m[i-1])
        return (max(m[i-1],n[j-1])+min(m[i],n[j]))/2 if even else min(m[i],n[j])
    else not (i>=len(m) or m[i] >= n[j-1]):
        startIndex = i+1
    else:
        endIndex = i-1
```
    
We need to prevent i<0 and i>=len(m) before handling if else statement with:  

refactoring and reviewing:

```
    if endIndex < 0 or startIndex >= len(m):
        i = ?
        j = ?
        return ?
    if (m[i] >= n[j-1]) and (i==0 or n[j] >= m[i-1])
        if i == 0 and len(m) == len(n):
            return (n[j-1]+m[i])/2
        elif i == 0:
            return (n[j-1]+min(m[i],n[j]))/2 if even else min(m[i],n[j])
        else:
            return (max(m[i-1],n[j-1])+min(m[i],n[j]))/2 if even else min(m[i],n[j])
    else m[i] < n[j-1]:
        startIndex = i+1
    else:
        endIndex = i-1            
```

finally we have:
```   
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
```          

General steps: 

-> redesign -> re-reasoning -> refactor ->  redesign -> ...
