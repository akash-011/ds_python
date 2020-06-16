#implementation of a Queue using list

queue = []

#Enqueue using append 
queue.append('a')
queue.append('b')
queue.append('c')

print(f'inital queue {queue}')

#dequeue using pop(0)
queue.pop(0)
queue.pop(0)

print(f'Queue after dequeing 2 elements {queue}')

#Iplementing a Queue using coleections.deque

from collections import deque

q = deque()

#Add elements using append
q.append('a')
q.append('b')
q.append('c')

print(f'inital queue {q}')
#dequeue elements using popleft()
q.popleft()
q.popleft()
print(f'Queue after dequeing 2 elements {q}')
