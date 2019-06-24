# eg. 
# numberOfNodes = 6
# existEdges = [[1,3],[2,4],[4,5]]
# numberOfNewRoutes = [[1,6,9],[1,4,8], [4,6,2], [3,4,4]]
# 1---6 cost 9, 1---4 cost 8, 4---6 cost 2, 3---4 cost 4
# return 6
#
# if not spanning all, return -1

class Solution:
    def minimalCost(self, numberOfNodes, existEdges, numberOfNewRoutes, availableNewRoutes):
        result = 0
        parents = [-1]*numberOfNodes
        for edge in existEdges:
            self.unionSet(parents, edge[0], edge[1])
        
        availableNewRoutes = sorted(availableNewRoutes, key=lambda s: s[2])
        for newRoutes in availableNewRoutes:
            if self.find_parent(parents, newRoutes[0]) != self.find_parent(parents, newRoutes[1]):
                result += newRoutes[2]
                self.unionSet(parents, newRoutes[0], newRoutes[1])

        if parents.count(-1) > 1:
            return -1
        else: 
            return result


    def find_parent(self, parent,i): 
        if parent[i] == -1: 
            return i 
        if parent[i]!= -1: 
             return self.find_parent(parent,parent[i]) 

    def unionSet(self, parents, x, y):
        x_set = self.find_parent(parents, x) 
        y_set = self.find_parent(parents, y) 
        parents[x_set] = y_set 

        
s=Solution()
# print(s.minimalCost(5, [[1,2],[1,3]], 3, [[4, 1, 3], [2, 0, 4], [3,4,2]]))

print(s.minimalCost(6, [[1,2],[1,3]], 3, [[4, 3, 7], [2, 0, 4], [5, 4, 1], [5, 0, 4]]))