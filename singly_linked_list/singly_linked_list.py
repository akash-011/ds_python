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
			current = None
		else:
			previous.set_next(current.get_next())
			current = None
	
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

	def reverse(self):
		current = self.head
		previous = None

		while current:
			nxt = current.get_next()
			current.next_node = previous
			previous = current
			current = nxt
		self.head = previous

	def merge_sorted(self, llist):
	
		ssl_1 = self.head 
		ssl_2 = llist.head
		s = None
	
		if not ssl_1:
			return ssl_2
		if not ssl_2:
			return ssl_1

		if ssl_1 and ssl_2:
			if ssl_1.get_data() <= ssl_2.get_data():
				s = ssl_1 
				ssl_1 = ssl_1.get_next()
			else:
				s = ssl_2
				ssl_2 = ssl_2.get_next()
			new_head = s 
		while ssl_1 and ssl_2:
			if ssl_1.get_data() <= ssl_2.get_data():
				s.set_next(ssl_1)
				s = ssl_1 
				ssl_1 = ssl_1.get_next()
			else:
				s.set_next(ssl_2)
				s = ssl_2
				ssl_2 = ssl_2.get_next()
		if not ssl_1:
			s.set_next(ssl_2) 
		if not ssl_2:
			s.set_next(ssl_1) 
	 
		return new_head

	def print_nth_last_node(self, n):

		#Method 1 
		# ssl_len =  self.len()
		# current = self.head
		# while current:
		# 	if ssl_len == n:
		# 		print(current.get_data())
		# 		return current
		# 	ssl_len -= 1
		# 	current = current.get_next()
		# 	if current is None:
		# 		return 
	
		#Method 2 - using 2 pointers 
		p = self.head 
		q = self.head 
		count = 0 

		while q and n>0:
			q = q.get_next()
			n = n-1
		
		
		if not q:
			print("Node not found")
		
		while p and q:
			p = p.get_next()
			q = q.get_next()
			
		return p.get_data()


	def rotate(self, k):
		p = self.head 
		q = self.head 
		prev = None
		count = 0 

		while p and count < k:
			prev = p
			p = p.get_next()
			q = q.get_next()
			count = count + 1
		p = prev

		while q:
			prev = q
			q = q.get_next()
		q = prev
		
		q.set_next(self.head)
		self.head = p.get_next()
		p.set_next(None)



if __name__ == "__main__":
	l1 = LinkedList()
	l1.append(1)
	l1.append(2)
	l1.append(3)
	l1.append(4)
	l1.append(5)
	l1.append(6)
	l1.rotate(4)
	