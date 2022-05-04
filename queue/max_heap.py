from heapq import heappop, heappush, heapify
"""
We use heapq class to implement Heaps in Python. By default Min Heap is implemented by this class. 
But we multiply each value by -1 so that we can use it as MaxHeap.
"""
heap = []
heapify(heap)

heappush(heap, -1 * 10)
heappush(heap, -1 * 20)
heappush(heap, -1 * 30)
heappush(heap, -1 * 40)
heappush(heap, -1 * 50)
heappush(heap, -1 * 60)

for i in heap:
    print(-1 * i)

element = heappop(heap)
print(element * -1)