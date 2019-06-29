
# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

# Note: You may not slant the container and n is at least 2.

# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example:

# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49



class Solution:
    def maxArea(self, height):
        i=0
        j=len(height)-1
        rtype=0
        while i < j:
            area = (j-i)* (height[i] if height[i] < height[j] else height[j])
            rtype = area if area > rtype else rtype
            if height[i] < height[j]:   #短边一侧向内移动， 才有可能形成大值， (width在缩小，短边不动，蓄水量一定在缩小)
                i+=1
            else:
                j-=1
        return rtype

#这题用brutal force是 Nx(N-1), O(N**2)
#以上的解法是线性的， O(N)
#思路： 从两边向中间， 这是一种宽度不断缩小的变化
# width==N-1 最大，只有一个值
# width==N-2, 两个值， 左边的桶边向右，或者右边的桶边向左，根据边长决定，只有变长大值，才有可能继续比较
# width==N-3, 依旧是两种可能，（因为之前的width==N-2已经淘汰小值的选择）
# ....
 


s=Solution()        
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
