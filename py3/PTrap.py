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
                        break;
                    else:
                        rtype+=(height[stack[-1]]-btmH)*(hi-stack[-1]-1)
                        btmH=height[stack.pop()]

                stack+=[hi]
        return rtype


pt = PTrap()
print pt.trap([0,1,0,2,1,0,1,3,2,1,2,1])