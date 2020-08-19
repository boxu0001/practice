'''
218. The Skyline Problem
Hard

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).
Buildings Skyline Contour

The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

    The number of buildings in any input list is guaranteed to be in the range [0, 10000].
    The input list is already sorted in ascending order by the left x position Li.
    The output list must be sorted by the x position.
    There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]
'''

from __future__ import annotations

import heapq
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        #这里的sort很关键，（在同一位置多个高度）让高点位的左侧线先处理，（如果在同一点左侧线右侧线都有）让右侧线后处理
        # [x, -h, y, True] 和 [y, h, y, False]
        bpq=sorted([[x, -h, y, True] for x, y, h in buildings] + [[y, h, y, False] for x, y, h in buildings])
        height=[[0, -1]]    #存的都是negtive height, 为了从大到小的priority
        result=[[-1, 0]]
        for x, negh, y, left in bpq:
            if left:
                #negh这里是negtive值,
                #由于有以上sort的处理，同点多高度情况，高点位先处理，所以会覆盖之后的同点低位
                heapq.heappush(height, [negh, y])
            else:
                #negh这里是事实上是positive值
                if y == height[0][1] and negh == -height[0][0]:
                    #由于有以上sort的处理，同点有左右线时，左线已被压上queue,所以高度相同不会重复，eg. 不会出现[2,9],[5,9]
                    while  0 <= height[0][1] <= y:
                        heapq.heappop(height)

            #由于有以上sort的处理，同点多高度 和 不同点同高度，处理都被简化
            if result[-1][1] != -height[0][0]:
                result += [[x, -height[0][0]]]
        return result[1:]
            
s=Solution()
r=s.getSkyline([[0,2,3],[2,5,3]])
print(r)