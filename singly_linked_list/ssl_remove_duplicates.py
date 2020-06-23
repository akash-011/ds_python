from singly_linked_list import LinkedList

def remove_duplicates(sll):

	my_dict = {}
	current = sll.head
	prev = None 

	while current:
		if current.get_data() in my_dict:
			prev.next_node = current.next_node
			current = None
		else:
			my_dict[current.get_data()] = 1
			prev = current

		current = prev.get_next()
	return ssl

if __name__ == "__main__":
	ssl = LinkedList()
	ssl.append('a')
	ssl.append('b')
	ssl.append('b')
	ssl.append('c')
	ssl.append('a')
	ssl.append('d')
	ssl.append('a')
	ssl.append('f')
	x = remove_duplicates(ssl)
	x.print_nodes()
	