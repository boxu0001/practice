class PTrap(object):
    def trap(self, height):
        rtype=0
        stack=[0]
        for hi in range(1, len(height)):
            btmH=height[stack[-1]]
            curH=height[hi]
            if curH < btmH:
                stack+=[hi]
            else:
                btmH=height[stack.pop()]
                while (len(stack) > 0):
                    if height[stack[-1]] > curH:
                        rtype+=(curH-btmH)*(hi-stack[-1]-1)
                        stack+=[hi]
                        break
                    else:
                        rtype+=(height[stack[-1]]-btmH)*(hi-stack[-1]-1)
                        btmH=height[stack.pop()]

                stack+=[hi]
        return rtype

    def trapNew(self, h):
        rst = 0
        i=0
        j=len(h)-1
        while i < j:
            testRes = (h[i] if h[i] < h[j] else h[j])*(j-i-1)
            rst = testRes if testRes > rst else rst
            if h[i] < h[j]:
                i+=1
            else:
                j-=1
        return rst
            
pt = PTrap()
# print(pt.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(pt.trapNew([0,1,0,2,1,0,1,3,2,1,2,1]))