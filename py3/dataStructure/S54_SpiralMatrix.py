# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
# Example 1:
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]

# Example 2:
# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

class Solution:
    def spiralOrder(self, matrix):
        result=[]
        rows=0
        rowe=len(matrix)-1
        if rowe == -1:
            return result
        cols=0
        cole=len(matrix[0])-1
        while rows <= rowe and cols <= cole:
            if rows == rowe:
                result += [i for i in matrix[rows][cols:cole+1]]
            else:
                result+=[i for i in matrix[rows][cols:cole]]

            if cols == cole and rows < rowe:                
                for i in range(rows, rowe+1):
                    result+=[matrix[i][cole]]
            else:
                for i in range(rows, rowe):
                    result+=[matrix[i][cole]]

            if rows < rowe:
                result+=[i for i in matrix[rowe][cole:cols:-1]]

            if cols < cole:    
                for i in range(rowe, rows, -1):
                    result+=[matrix[i][cols]]
            rows+=1
            rowe-=1
            cols+=1
            cole-=1
        return result
s=Solution()        
print(s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
print(s.spiralOrder([[1, 2, 3],[4, 5, 6], [7,8,9]]))
print(s.spiralOrder([[1],[3]]))
print(s.spiralOrder([[2,4,6]]))
print(s.spiralOrder([[2],[3],[4]]))
print(s.spiralOrder([[0]]))
print(s.spiralOrder([[1],[2],[3],[4],[5], [6]]))