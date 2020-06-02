class Node(object):
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next_node = next_node

	def get_data(self):
		return self.data
	
	def get_next(self):
		return self.next_node
	
	def set_next(self, new_next):
		self.next_node = new_next

class LinkedList(object):
	def __init__(self, head=None):
		self.head = head 
	
	#insert new node at head of linked list 
	def prepend(self, data):
		new_node = Node(data)
		new_node.set_next(self.head)
		self.head = new_node 
	
	def size(self):
		current = self.head
		count = 0
		while current:
			count += 1
			current = current.get_next()
		return count
	
	def search(self, data):
		current = self.head
		found = False 
		while current and found is False:
			if current.get_data() == data:
				found = True
			else:
				current = current.get_next()
		if current is None:
			raise ValueError("Data not in list")
		return current  

	def delete(self, data):
		current = self.head 
		found = False
		previous = None
		while current and found is False:
			if current.get_data() == data:
				found = True 
			else:
				previous = current 
				current = current.get_next()
		if current is None:
			raise ValueError("Data not found")
		if previous is None:
			self.head = current.get_next()
		else:
			previous.set_next(current.get_next())
	
	def print_nodes(self):
		current = self.head
		while current:
			print(current.get_data())
			current = current.get_next()
	
	#add node to the tail of the list
	def append(self, data):
		new_node = Node(data)

		if self.head is None:
			self.head = new_node
			return
		
		last_node = self.head
		while last_node.next_node:
			last_node = last_node.get_next()
		last_node.set_next(new_node)

	def insert(self,prev_node, data):
		if not prev_node:
			print("Prev Node doesnt exist")

		new_node = Node(data)
		new_node.set_next(prev_node.next_node)
		prev_node.set_next(new_node)

		


llist = LinkedList()
llist.append('A')
llist.append('B')
llist.append('C')
llist.append('D')
llist.insert(llist.head.next_node, 'E')
llist.print_nodes()