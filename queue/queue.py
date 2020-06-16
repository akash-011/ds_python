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