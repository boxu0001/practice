#1. given two list, A: [(1, 100), (2, 300), (5, 800) ...], B: [(4, 900), (3, 600)...]
#each element is a tuple: (id, value)
#2. given a Max value m, find a list of ids tuples, such corresponding ValueA + ValueB <= m and close to m

class solution:
    def closestSum(self, mx, x, y):
        result=[]
        if not x or not y:
            return result
        sortKey = lambda i: i[1]
        x.sort(key=sortKey)
        y.sort(key=sortKey)
        
        j = len(y)-1                                # inintialize 
        currentMx = None
        for xi in x:                                # 思路是基于xi, 找到当前最优解， (xi, yj), 满足以下条件
                                                    # 1. (xi， yj+1) 一定不满足， 2. Value(xi, yj) < Value(xi+1, yj)
                                                    # 所以算法是让yj线性递减， xi线性增加， O(X+Y)
            xId, xValue = xi
            while j >=0 and xValue+y[j][1] > mx:    # iterate b from right to left, find max(xValue+yValue) <= mx
                j-=1
            if j < 0:                               # we don't find any pairs
                return result
            yId, yValue = y[j]                      # we find a candidate pair
            currentSum = xValue + yValue            #这里需要考虑最优解， currentMx是当前最优值，(注意 如果允许重复的值， 这里要用循环去找接下来可能重复的 Yj-1, Yj-2, .. == Yj )
            if currentMx == None or currentSum == currentMx:    #如果等于当前最优值， 加到result list里
                result+=[(xId, yId)]
                currentMx = currentSum
            elif currentSum > currentMx:                        #如果大于当前最优值， 整个result list要被替换
                result=[(xId, yId)]
                currentMx = currentSum
            else:                                               #小于的情况， 忽略
                pass
        return result

s=solution()
r=s.closestSum(1000, [(1, 100), (2, 300), (5, 800)],  [(4, 900), (3, 700)])
print(r)
print(s.closestSum(1100, [(1, 100), (2, 300), (5, 800)],  []))




