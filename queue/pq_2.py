#Priority Queue implementation using lists 
class PriorityQueue(object):
	def __init__(self):
		self.pq = []
	
	def is_empty(self):
		return len(self.pq) == 0
	
	def insert(self, data):
		self.pq.append(data)
	
	def remove(self):
		max = 0 
		try:
			for i in range(len(self.pq)):
				if self.pq[i] > self.pq[max]:
					max = i
			item = self.pq[max]
			del self.pq[max]
			return item 
		except IndexError():
			print()
			exit()

if __name__ == "__main__":
	pq = PriorityQueue() 
	pq.insert(12) 
	pq.insert(1) 
	pq.insert(14) 
	pq.insert(7) 
	print(pq)             
	while not pq.is_empty(): 
		print(pq.remove())
