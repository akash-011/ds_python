"""
https://leetcode.com/problems/last-stone-weight/

"""
import heapq

def last_stone_weight(stones):
    stones_pq = [x*-1 for x in stones]
    heapq.heapify(stones_pq)
    print(stones_pq)

    while len(stones_pq) > 1:
        x = heapq.heappop(stones_pq) * -1
        y = heapq.heappop(stones_pq) * -1
        if x > y:
            heapq.heappush(stones_pq, (x-y)*-1)
        elif x < y:
            heapq.heappush(stones_pq, (y-x)*-1)

        heapq.heapify(stones_pq)
        print(stones_pq)

    if len(stones_pq) > 0:
        return stones_pq[0] * -1
    else:
        return 0

print(last_stone_weight([2,7,4,1,8,1]))