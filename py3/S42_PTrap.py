# 42. Trapping Rain Water
# Hard

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

# Example:

# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6


class PTrap(object):
    def trap(self, height):
        rtype=0
        stack=[0]                           #栈初始化， 放入水池的左边边界和底部索引， [left1, left2, ...., leftK, bottom]
        for hi in range(1, len(height)):    # S1 hi 是索引
            btmH=height[stack[-1]]          # S2 初始化底部高度
            curH=height[hi]                 # 当前边界高度
            if curH < btmH:                 # a. 如果当前边界小于当前底部， 栈里保持持续下降
                stack+=[hi]
            else:
                btmH=height[stack.pop()]    # b. 如果当前边界大于水池底部，抛出最近的边界，形成底部
                while (len(stack) > 0):                 # b.1 循环，如果栈不空，开始计算水量
                    if height[stack[-1]] > curH:            # b.1.c 当前还是会变成新底部 在S2中，
                        rtype+=(curH-btmH)*(hi-stack[-1]-1)     #累加蓄水量
                        stack+=[hi]                             #b.1.c.1 加栈 变成新底部 保持边界持续下降
                        break
                    else:                                   # b.1.d 形成右边界， 注意， 这个右边界没有加入栈， 循环b.1会继续比较， 
                        rtype+=(height[stack[-1]]-btmH)*(hi-stack[-1]-1)    # 当前边界和左边界形成蓄水 累加蓄水量
                        btmH=height[stack.pop()]                            # b.1.d.1 抛栈 抛出旧底部， 形成新底部

                stack+=[hi]                             # b.2 如果栈空了 （由b.1.d.1造成 当前边界为当前最大值）, 加栈
        return rtype


pt = PTrap()
print(pt.trap([0,1,0,2,1,0,1,3,2,1,2,1]))