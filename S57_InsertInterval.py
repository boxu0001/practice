# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
# You may assume that the intervals were initially sorted according to their start times.
# Example 1:
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

# Example 2:
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        result=[]
        consumed=False
        for i in intervals:
            if not consumed:
                if newInterval.end < i.start:
                    result+=[[newInterval.start, newInterval.end]]
                    result+=[[i.start, i.end]]
                    consumed = True
                elif newInterval.start > i.end:    
                    result+=[[i.start, i.end]]
                else:    
                    s=min(newInterval.start, i.start)
                    e=max(newInterval.end, i.end)
                    result+=[[s, e]]
                    consumed = True
            else:
                if result[-1][1] >= i.start:
                    result[-1][1] = max(result[-1][1], i.end)        
                else:
                    result+=[[i.start, i.end]]    
        if not consumed:
            result+=[[newInterval.start, newInterval.end]]        

        return result
s=Solution()        
print(s.insert([Interval(1, 2), Interval(3, 5), Interval(6, 7), Interval(8, 10), Interval(12, 16)], Interval(4, 8)))
print(s.insert([Interval(1, 3), Interval(6, 9)], Interval(2, 5)))