'''
347. Top K Frequent Elements
Medium

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

Note:

    You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
    Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
    It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
    You can return the answer in any order.
'''
import heapq as pq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        queue=[]
        count={}
        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1
        for n in count:
            if len(queue) < k :
                pq.heappush(queue, (count[n], n))
            elif len(queue) == k and count[n] > queue[0][0]:
                pq.heapreplace(queue, (count[n], n))
            else:
                pass

        return [n for _,n in queue]