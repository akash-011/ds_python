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
	def insert(self, data):
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

my_list = LinkedList()
my_list.insert(1)
my_list.insert(2)
my_list.insert(3
my_list.print_nodes()
search_node = my_list.search(1)
print(search_node.get_data())



