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
	
	def delete_with_position(self, position):
		current = self.head
		previous = None
		if position == 0:
			self.head = current.get_next()
			current = None
			return
		count = 0
		while current and count != position:
			previous = current
			current = current.get_next()
			count += 1
		
		if current is None:
			print("Node not found")
			return
		
		previous.set_next(current.get_next())
		current = None

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
			return

		new_node = Node(data)
		new_node.set_next(prev_node.next_node)
		prev_node.set_next(new_node)

	def len(self):
		count = 0
		current = self.head
		while current:
			count += 1
			current = current.get_next()
		return count

	def len_recursive(self, node):
		if node is None:
			return 0
		return 1 + self.len_recursive(node.get_next())
		
	def node_swap(self, key_1, key_2):
		if key_1 == key_2:
			return
		
		current_1 = self.head
		previous_1 = None

		while current_1 and current_1.get_data() != key_1:
			previous_1 = current_1
			current_1 = current_1.get_next()

		current_2 = self.head
		previous_2 = None
		while current_2 and current_2.get_data() != key_2:
			previous_2 = current_2
			current_2 = current_2.get_next()

		if not current_2 or not current_1:
			return
		
		if previous_1:
			previous_1.next_node = current_2
		else:
			self.head = current_2

		if previous_2:
			previous_2.next_node = current_1
		else:
			self.head = current_1
		
		current_1.next_node, current_2.next_node = current_2.next_node, current_1.next_node





llist = LinkedList()
llist.append('a')
llist.append('b')
llist.append('c')
llist.append('d')
llist.prepend('x')
llist.node_swap('a', 'x')
llist.print_nodes()