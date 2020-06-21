'''
212. Word Search II
Hard

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example:

Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]

 

Note:

    All inputs are consist of lowercase letters a-z.
    The values of words are distinct.
'''
from __future__ import annotations
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m=len(board)
        n=len(board[0]) if board else 0
        result=[]
        visited=[[False]*n for _ in range(m)]
        tries=self.buildTries(words)

        for i in range(m):
            for j in range(n):
                s1 = []
                s2 = []
                nx, ny = i, j
                while True:
                    if nx != None and ny != None:
                        #test nx, ny
                        if m>nx>=0 and n>ny>=0 and not visited[nx][ny]:
                            nset=[]
                            s2top = s2[-1] if len(s2) > 0 else tries
                            #using tries
                            if board[nx][ny] in s2top:
                                visited[nx][ny]=True
                                s1+=[[nx,ny]]
                                s2+=[s2top[board[nx][ny]]]
                                if "END" in s2top[board[nx][ny]]:
                                    result+=[s2top[board[nx][ny]]["END"]]
                                    s2top[board[nx][ny]].pop("END")
                                #init to the LEFT point of current point
                                nx,ny=nx,ny-1
                            else:
                                #try next nx, ny
                                nx, ny = self.getNextTry(s1, nx, ny)
                                
                        else:
                            #try next nx, ny
                            nx, ny = self.getNextTry(s1, nx, ny)
        
                    else:
                        #rollback
                        if len(s1) > 0:
                            nx,ny=s1.pop()
                            s2poped = s2.pop()
                            if len(s2poped) == 0:
                                s2Top=s2[-1] if len(s2) > 0 else tries
                                s2Top.pop(board[nx][ny])
                            visited[nx][ny]=False
                            #try next nx, ny
                            nx, ny = self.getNextTry(s1, nx, ny)
                        else:
                            break
            
        return result
    
    #rotate from TOP -> RIGHT ->BOTTOM
    def getNextTry(self, s1, nx, ny):
        if len(s1) > 0:
            x0, y0=s1[-1]
            if nx==x0 and ny==y0-1:
                nx, ny=x0-1, y0
            elif nx==x0-1 and ny==y0:
                nx, ny=x0, y0+1
            elif nx==x0 and ny==y0+1:
                nx, ny=x0+1, y0
            else:
                nx, ny=None, None
        else:
            nx, ny=None, None
        return nx, ny

    def buildTries(self, words: List[str]) -> Map:
        root={}
        for wd in words:
            itr = root
            for c in wd:
                if c not in itr:
                    itr[c]={}
                itr=itr[c]
            itr["END"]=wd
        return root



s=Solution()
# s.buildTries(["abcd", "abk", "lmn"])
s.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],["oath","pea","eat","rain"])
