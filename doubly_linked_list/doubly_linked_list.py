class Node(object):

    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node
    
    def get_next(self):
        return self.next_node
    
    def get_data(self):
        return self.data 
    
    def get_prev(self):
        return self.prev_node
    
    def set_next(self, new_next):
        self.next_node = new_next
    
    def set_prev(self, new_prev):
        self.prev_node = new_prev

class DoublyLinkedList(Node):

    def __init__(self):
        self.head = None 
    
    def append(self, data): 

        new_node = Node(data)

        if self.head is  None:
            self.head = new_node
        else:
            current = self.head

            while current.get_next():
                current = current.get_next()

            current.set_next(new_node)
            new_node.set_prev(current)

    def prepend(self, data):

        new_node = Node(data)
        if self.head:
            new_node.set_next(self.head)
            self.head.set_prev(new_node)
            self.head = new_node
        else:
            self.head = new_node

    def delete(self, data):
        
        current = self.head 
        while current:
            if current.get_data() == data and current == self.head:
                if not current.get_next():
                    current = None 
                    self.head = None
                    return 
                else:
                    nxt = current.get_next()
                    current.set_next(None)
                    current = None 
                    nxt.set_prev(None)
                    self.head = nxt
                    return 
                
            elif current.get_data() == data:
                if current.get_next():
                    prev = current.get_prev()
                    nxt = current.get_next()
                    prev.set_next(nxt)
                    nxt.set_prev(prev)
                    current.set_next(None)
                    current.set_prev(None)
                    current = None 
                    return
                else:
                    prev = current.get_prev()
                    prev.set_next(None)
                    current.set_prev(None)
                    current = None 
                    return

            current = current.get_next()





                    
        

    def add_node_after(self, data, key):

        current = self.head
 
        while current:
            if current.get_next() is None and current.get_data() == key:
                self.append(data)
                return
            elif current.get_data() == key:
                new_node = Node(data)
                next_node = current.get_next()
                current.set_next(new_node)
                new_node.set_next(next_node)
                new_node.set_prev(current)
                next_node.set_prev(new_node)

            current = current.get_next()

    def add_node_before(self, data, key):

        current = self.head

        while current:
            if current.get_next() is None and current.get_data() == key:
                self.prepend(data)
                return
            elif current.get_data() == key:
                new_node = Node(data)
                prev = current.get_prev()
                prev.set_next(new_node)
                new_node.set_prev(prev)
                new_node.set_next(current)
                current.set_prev(new_node)
            
            current = current.get_next()

    def print_list(self):

        current = self.head
        while current:
            print(current.get_data())
            current = current.get_next()
        

if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append('a')
    dll.append('b')
    dll.append('c')
    dll.prepend('x')
    dll.delete('c')
    dll.print_list()

        