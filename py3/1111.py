from __future__ import annotations
import heapq
class Solution:
    def getMinScore(self, products_nodes, products_from, products_to):
        # Write your code here
        result=None
        matrix=[{} for _ in range(products_nodes+1)] #matrix[0] is not used
        n=len(products_from)
        for i in range(n):  #
            matrix[products_from[i]].add(matrix[products_to[i]])
            matrix[products_to[i]].add(matrix[products_from[i]])

        #find trios
        for i in range(1, products_nodes+1):
            for j in matrix[i]:
                for k in matrix[j]:
                    if k != i and i in matrix[k]:
                        tmpSum = len(matrix[i]) + len(matrix[j]) + len(matrix[k]) - 6
                        if result==None or result > tmpSum:
                            result = tmpSum
        
        return tmpSum

def fun():
    return False


# s=Solution()
# s.m1()

print(fun())

