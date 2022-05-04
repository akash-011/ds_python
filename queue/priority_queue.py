#Priority Queue Implementation using heapq(min heapq). heappush used to add elements and heappop used to remove elements in order
import heapq

my_pq = []

heapq.heappush(my_pq,(3, "Wayne"))
heapq.heappush(my_pq,(2, "Marcus"))
heapq.heappush(my_pq,(5, "Phil"))
heapq.heappush(my_pq,(1, "Paul"))

while my_pq:
	print(my_pq)
	print(heapq.heappop(my_pq))
