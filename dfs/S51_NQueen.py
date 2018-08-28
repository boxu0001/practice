# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
# Given an integer n, return all distinct solutions to the n-queens puzzle.
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
# Example:
# Input: 4
# Output: [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],

#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
class Solution:
    def solveNQueens(self, n):
        nj=0
        stack=[]
        result=[]
        colms=[False]*n         #j
        diagx=[False]*(2*n-1)   #i+j
        diagy=[False]*(2*n-1)   #n-1+j-i

        while n>nj>=0:
            stack+=[nj]
            i=len(stack)-1
            colms[nj]=True
            diagx[i+nj]=True
            diagy[n-1+nj-i]=True
            nj=0 #set next nj to 0
            if len(stack) == n:
                result+=[['.'*i+'Q'+'.'*(n-1-i) for i in stack]]
                j=stack.pop()
                colms[j]=False
                diagx[n-1+j]=False
                diagy[j]=False
                nj=n
            ni=len(stack)
            while((nj==n or colms[nj] or diagx[ni+nj] or diagy[n-1+nj-ni]) and len(stack)>0):
                #rollback or nj++
                if nj < n:
                    nj+=1
                else:
                    j=stack.pop()
                    ni-=1
                    colms[j]=False
                    diagx[ni+j]=False
                    diagy[n-1-ni+j]=False
                    nj=j+1
        return result


s=Solution()
print(s.solveNQueens(4))
