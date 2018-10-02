'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''
import unittest

class Solution(unittest.TestCase):
    def exist(self, board, word):
        m=len(board)
        if m==0:
            return False if len(word) > 0 else True
        n=len(board[0])
        if n==0:
            return False if len(word) > 0 else True
        nix=(0, 0)
        stack=[]
        while(nix != None):
            i, j = nix
            if nix in stack or i < 0 or i >= m or j < 0 or j >= n or word[len(stack)] != board[i][j]:
               
                #next available
                while(len(stack) > 0 and i == stack[-1][0] + 1):
                    i, j = stack.pop()
                if len(stack) == 0:
                    if j < n-1:
                        j+=1
                    else:
                        i+=1
                        j=0
                    nix = (i, j) if i <= m-1 else None
                elif i ==  stack[-1][0]-1 and j == stack[-1][1]:
                    nix = (stack[-1][0],  stack[-1][1]-1)
                elif i == stack[-1][0] and j == stack[-1][1]-1: 
                    nix = (stack[-1][0],  stack[-1][1]+1)
                elif i == stack[-1][0] and j == stack[-1][1]+1:
                    nix = (stack[-1][0]+1, stack[-1][1])
            else:
                stack+=[nix]
                if len(stack) == len(word):
                    return True
                if i > 0:
                    nix = (i-1, j)
                elif j > 0:
                    nix = (i, j-1)
                elif j < n-1:
                    nix = (i, j+1)
                else:
                    nix = (i+1, j)

        return False
        
    def test1(self):
        b=[['A','B','C','E'],
            ['S','F','C','S'],
            ['A','D','E','E']]
        r1=self.exist(b, "ABCCED")
        self.assertEqual(True, r1)

        r2=self.exist(b, "SEE")
        self.assertEqual(True, r2)

        r3=self.exist(b, "ABCB")
        self.assertEqual(False, r3)

        self.assertEqual(False, self.exist([['a']],'ab'))
        self.assertEqual(False, self.exist([['a', 'b'], ['c', 'd']],'abcd'))




if __name__ == '__main__':
    unittest.main()