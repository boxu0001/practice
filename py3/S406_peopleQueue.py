'''
406. Queue Reconstruction by Height
Medium

Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.
 

Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
'''
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        result=[]
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        for p in people:
            result.insert(p[1], p)
            
        return result

#先插高度最高的，因为后插入的高度低的对前面的次序值不产生作用
#插入的次序为前面的高个的个数
#例如： 
#   0       1       2       3       4       5
#-------------------------------------------------
#   7,0     7,1     
#           ^
#   7,0     6,1     7,1
#           ^
#   5,0     7,0     6,1     7,1
#   ^
#   5,0     7,0     5,2     6,1     7,1
#                   ^
#   5,0     7,0     5,2     4,4     6,1     7,1
#                           ^

