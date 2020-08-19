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

class CircularLinkedList(Node):

    def __init__(self):
        self.head = None
    
    def append(self, data):

        if not self.head:
            self.head = Node(data)
            self.head.set_next(self.head)
        else:
            new_node = Node(data)
            current = self.head
            while current.get_next() != self.head:
                current = current.get_next()
            current.set_next(new_node)
            new_node.set_next(self.head)
    
    def print_list(self):

        current = self.head
        while current:
            print(current.get_data())
            current = current.get_next()
            if current == self.head:
                break
    
    def prepend(self, data):

        new_node = Node(data)
        current = self.head
        new_node.set_next(self.head)

        if not self.head:
            new_node.set_next(new_node)
        else:
            while current.get_next() != self.head:
                current = current.get_next()
            current.set_next(new_node)
        self.head = new_node


if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.append('a')
    cll.append('b')
    cll.prepend('A')
    cll.prepend('B')
    cll.print_list()