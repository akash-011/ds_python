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
    
    def reverse(self):

        temp = None 
        current = self.head 
        while current:
            temp = current.get_prev()
            current.set_prev(current.get_next())
            current.set_next(temp)
            current = current.get_prev()
        if temp:
             self.head = temp.get_prev()
    
    def delete_node(self, node):

        current = self.head 
        while current:
            if current == node and current == self.head:
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
                
            elif current == node:
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


    def remove_duplicates(self):
        
        hash_table = {}
        current = self.head 
        while current:
            if current.get_data() not in hash_table:
                hash_table[current.get_data()] = 1
                current = current.get_next()
            else:
                nxt = current.get_next()
                self.delete_node(current)
                current = nxt 
    
    def pair_with_sum(self, total):

        pairs = []
        current = self.head 
        q = None

        while current:
            q = current.get_next()
            while q:
                if current.get_data() + q.get_data() == total:
                    pairs.append("(" + str(current.get_data()) + "," + str(q.get_data()) + ")")
                q =  q.get_next()
            current = current.get_next()
        
        return pairs

  

if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    print(dll.pair_with_sum(5))

        