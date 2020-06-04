class Stack(object):
	def __init__(self):
		self.items = []
	
	def push(self, item):
		self.items.append(item)
	
	def pop(self):
		return self.items.pop()
	
	def peek(self):
		if not self.is_empty():
			return self.items[-1]
	
	def is_empty(self):
		return self.items == []
	
	def get_stack(self):
		return self.items

# in python , lists can be used as stacks or deque form collection or LifoQueue from Queue