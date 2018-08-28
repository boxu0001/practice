# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
# Example:
# Input: [1,1,2]
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]

class Solution:
    def permuteUnique(self, sublist):
        lsb = len(sublist)
        if lsb <= 1:
            return [sublist if lsb==1 else []]
        else:
            result = []
            p0list = self.permuteUnique(sublist[1:])
            for e in p0list:
                    result += [[sublist[0]] + e]
            i=1
            swapped={sublist[0]}
            while(i<lsb):
                if sublist[i] not in swapped :
                    #swap and recursiveP
                    anewlist=sublist[1:]
                    anewlist[i-1] = sublist[0]
                    plist = self.permuteUnique(anewlist)
                    for e in plist:
                        result += [[sublist[i]] + e]
                    swapped.add(sublist[i])
                i+=1
            return result   

s = Solution()
print(s.permuteUnique([1,1]))
