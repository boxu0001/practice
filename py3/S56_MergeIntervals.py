# Given a collection of intervals, merge all overlapping intervals.
# Example 1:
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

# Example 2:
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considerred overlapping.

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        result=[]
        intervals.sort(key=lambda i:i.start)
        for i in intervals:
            if len(result) == 0 or result[-1][1] < i.start:
                result+=[[i.start, i.end]]
            else:
                result[-1][1] = i.end if i.end > result[-1][1] else result[-1][1]
        return result


s=Solution()
print(s.merge([]))
print(s.merge([Interval(1,4),Interval(4,5)]))
print(s.merge([Interval(1,3),Interval(2,6),Interval(8,10),Interval(15,18)]))

