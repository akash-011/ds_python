from singly_linked_list import LinkedList

def count_occurencces(ssl, data):
	count = 0 
	current = ssl.head
	while current:
		if current.get_data() == data:
			 count += 1
		current = current.get_next()

	return count 

def count_occurencces_recursive(ssl, node, data):
	if not node:
		return 0
	if node.get_data() == data:
		return 1 + count_occurencces_recursive(ssl, node.next_node, data)
	else:
		return count_occurencces_recursive(ssl, node.next_node, data)

if __name__ == "__main__":
	ssl = LinkedList()
	ssl.append(1)
	ssl.append(2)
	ssl.append(1)
	ssl.append(4)
	ssl.append(5)
	ssl.append(1)
	ssl.append(9)
	ssl.append(1)
	print(count_occurencces_recursive(ssl, ssl.head, 1))
	