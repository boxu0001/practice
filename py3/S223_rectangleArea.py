'''
223. Rectangle Area
Medium

Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area

Example:

Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45

Note:
'''
from __future__ import annotations
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        total=(C-A)*(D-B) + (G-E)*(H-F)        
        
        if C<=E or G<=A or D <= F or H <= B:
            return total
        
        xlist = sorted([A, C, E, G])
        ylist = sorted([B, D, F, H])
        total -= (xlist[2] -xlist[1]) * (ylist[2] -ylist[1])
        
        return total
