'''
Given the number of five-star and total reviews for each product a company sells, as well as the threshold percentage, what is the minimum number of additional five-star reviews the company needs to become five star seller.
For ex, there are 3 products (n=3) with productRatings =[[4,4],[1,2],[3,6]], percentage rating threshold = 77.
[1,2] indicates => [1 (five star reviews) ,2 (total reviews)].
We need to get the seller reach the threshold with minimum number of additional five star reviews.

Before we add more five star reviews, the percentage for this seller is ((4/4) + (1/2) + (3/6))/3 = 66.66%
If we add a five star review to 2nd product, ((4/4) + (2/3) + (3/6))/3 = 72.22%
If we add another five star review to 2nd product, ((4/4) + (3/4) + (3/6))/3 = 75%
If we add a five star review to 3rd product, ((4/4) + (3/4) + (4/7))/3 = 77.38%
At this point, 77% (threshold) is met. Therefore, answer is 3 (because that is the minimum five star reviews we need to add, to get the seller reach the threshold).

public static int fiveStarReviews(List<List<Integer>> productRatings, int ratingsThreshold){
}

Constraints:
1<= productRatings.size() <=200
In product ratings, [fivestar, total], fivestar <=100, total<=100
1<=ratingsThreshold< 100
productRatings contains only non negative integers.
'''
import heapq as pq
class Solution:
    def fiveStarReviews(self, productRatings, ratingsThreshold: float) -> int:
        queue=[]
        t=0
        for [x, y] in productRatings:
            pq.heappush(queue, [(x-y)/(y*(y+1)), x, y])
            t+=x/y
        
        N = len(productRatings)
        count=0
        T=ratingsThreshold*N

        while t < T:
            delta, x, y = pq.heappop(queue) #delta is a negtive, 
            t+=-delta
            pq.heappush(queue, [(x-y)/((y+2)*(y+1)), x+1, y+1])
            count+=1

        return count

s=Solution()
s.fiveStarReviews([[2,4],[1,2]], 0.8)