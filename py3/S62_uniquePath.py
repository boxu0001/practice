# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?


# Above is a 7 x 3 grid. How many possible unique paths are there?

# Note: m and n will be at most 100.

# Example 1:

# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right

# Example 2:

# Input: m = 7, n = 3
# Output: 28

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        f=[[0]*(m+1) for _ in range(n+1)]
        f[1][1]=1   #[1,1] in fact is the starting point, all the f[0][*] == f[*][0] = 0, are extra auxilary boundary, for easy coding
        for j in range(1, n+1):
            for i in range(1, m+1):
                if j > 1 or i > 1:
                    f[j][i] = f[j-1][i]+f[j][i-1]
        return f[n][m]
#总结：
#用到组合公式： C(m,n) = C(m-1, n) + C(m-1, n-1)
#一共走m+n-2步，要选择 m-1步向右走 （或n-1布向下走）
# C(m+n-2, m-1) = C(m+n-3, m-1) + C(m+n-3, m-2)



