class Solution:
    def shortestPalindrome(self, s: str) -> str:
        ls=len(s)
        midLeft=ls//2
        midRight=midLeft
        #从中间开始，
        while True:
            #把相同的字符区域拓展开，s[midLeft:midRight]都是同一字符
            while midLeft>=1 and s[midLeft] == s[midLeft-1]: midLeft-=1
            while midRight<ls-1 and s[midRight+1] == s[midLeft]: midRight+=1
            
            #当中间区域确定后，再比较左右两边
            l,r=midLeft, midRight
            while l>=0 and r<ls and s[l] == s[r]:
                l-=1
                r+=1
            #如果left到头了，就找到了最大sub-parlingdrom
            if l<0:
                return s[r:][::-1]+s
            #如果没到头，说明当前的s[midLeft:midRight]不适合做中间区域，需要向左移动，继续找
            else:
                #这里midLeft从上一个左边界的前一个字符开始，（X-midLeft-mid-midRight-Y, 不需要从mid-1开始，因为从 midLeft 到 mid-1一定不符合， 对称性和抽屉原理，X != middle char）
                midLeft -=1
                midRight = midLeft

