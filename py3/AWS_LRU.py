'''
A virtual memory management system in an operating system at Amazon can use LeastRecently-Used (LRU) cache. When a requested memory page is not in the cache and the cache is full, the page that was least-recently-used should be removed from the cache to make room for the requested page. If the cache is not full, the requested page can simply be added to the cache and considered the most-recently-used page in the cache. A given page should occur at most once in the cache.

Given the maximum size of the cache and a list of page requests, write an algorithm to calculate the number of cache misses. A cache miss occurs when a page is requested and isn't found in the cache.

Input

The input to the function/method consists of three arguments:

num, an integer representing the number of pages;

pages, a list of integers representing the pages requested;

maxCacheSize, an integer representing the size of the cache.

Output

Return an integer representing the number of cache misses.

Note

The cache is initially empty and the list contains pages numbered in the range 1-50. A page at index "i" in the list is requested before a page at index "i+1".

Constraints

0 <= i < num

Example

Input:

num = 6

pages = [1,2,1,3,1,2]

maxCacheSize = 2

Output:

4

Explanation:

Cache state as requests come in ordered longest-time-in-cache to shortest-time-in-cache:

1*

1,2*

2,1

1,3*

3,1

1,2*

Asterisk (*) represents a cache miss. Hence, the total number of a cache miss is 4.
'''

from __future__ import annotations

class Solution:
    def lruCacheMisses(self, pages: List(int), maxCacheSize: int) -> int:

        forward=[None] * 11
        backward=[None] * 11

        forward[0] = -1
        backward[0] = -1

        size=0

        count = 0
        for p in pages:
            if forward[p] == None:
                #not found, add or remove add
                count+=1
                if size == maxCacheSize:
                    x = forward[0]
                    forward[0] = forward[x]
                    forward[x] = None
                    backward[forward[0]] = -1
                    size-=1


                flast = 0 if backward[0] < 0 else backward[0]
                forward[flast] = p
                forward[p] = -1
                backward[p] = backward[0]
                backward[0] = p
                size+=1

            else: #found
                ti = forward[p]
                bi = 0 if backward[p] < 0 else backward[0]
                forward[bi] = forward[p]
                forward[backward[0]] = p
                forward[p] = -1

                backward[ti] = backward[p]
                backward[p] = backward[0]
                backward[0] = p

        return count


    #cache[0] cache[51]是空指针，cache[p][0] 是previous, cache[p][1]是 next
    # 0<=p<50
    def lruCacheMisses2(self, MAX: int, pages: List(int), maxCacheSize: int) -> int:
        TAIL=MAX+1
        cache=[[None, None] for _ in range(MAX+2)]
        cache[0][1] = TAIL    #这里初始化空头指向空尾
        cache[TAIL][0] = 0    #空尾指向空头， 防止在删除和加入的时候出想无指向
        size=0
        count=0
        for p in pages:
            if cache[p][0] == None and cache[p][1] == None:
                #not found
                count+=1
                if size == maxCacheSize:
                    #remove first, 
                    firsti = cache[0][1]
                    nxti = cache[firsti][1]
                    cache[0][1] = nxti
                    cache[nxti][0] = 0
                    cache[firsti][0] = None
                    cache[firsti][1] = None
                    size-=1
            else:
                #remove p
                pre, nxt = cache[p]
                cache[pre][1] = nxt
                cache[nxt][0] = pre
                cache[p][0]=None
                cache[p][1]=None
                size-=1

            #add p
            lasti = cache[TAIL][0]
            cache[TAIL][0] = p
            cache[lasti][1] = p
            cache[p][0] = lasti
            cache[p][1] = TAIL
            size+=1
        return count

s=Solution()

s.lruCacheMisses2(5, [1,2,3,4,2,1,3], 3)



