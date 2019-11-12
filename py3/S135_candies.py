'''
135. Candy
Hard

There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

    Each child must have at least one candy.
    Children with a higher rating get more candies than their neighbors.

What is the minimum candies you must give?

Example 1:

Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:

Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two conditions.

'''

class Solution:
    def candy(self, ratings: List[int]) -> int:
        c=[1 for _ in ratings]
        ls=len(ratings)
        for i in range(1, ls):      #从左边上升遍历
            if ratings[i] > ratings[i-1]:
                c[i] = c[i-1]+1
        
        for j in range(ls-2, -1, -1):
            if ratings[j] > ratings[j+1]:   #从右边上升遍历，然后update顶点值
                c[j] = max(c[j], c[j+1]+1)
        return sum(c)
        