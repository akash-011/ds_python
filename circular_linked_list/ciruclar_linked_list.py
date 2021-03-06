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
    

    def delete(self, data):

        if self.head.get_data() == data:
            current = self.head
            while current.get_next() != self.head:
                current = current.get_next()
            current.set_next(self.head.get_next())
            self.head = self.head.get_next()
        else:
            current = self.head
            prev = None
            while current.get_next() != self.head:
                prev = current
                current = current.get_next()
                if current.get_data() == data:
                    prev.set_next(current.get_next())
                    current = current.get_next()

    def __len__(self):

        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
            if current == self.head:
                break
        return count 

    def split_list(self):
        
        size = len(self)

        if size == 0:
            return None
        if size == 1:
            return self.head
        
        mid_point = size/2
        count = 0

        current = self.head
        prev = None

        while current and count < mid_point:
            count +=1 
            prev = current 
            current = current.get_next()
        prev.set_next(self.head)

        split_list = CircularLinkedList()

        while current.get_next() != self.head:
            split_list.append(current.get_data())
            current = current.get_next()
        split_list.append(current.get_data())

        self.print_list()
        print('\n')
        split_list.print_list()
    
    def remove_node(self, node):

        if self.head == node:
            current = self.head
            while current.get_next() != self.head:
                current = current.get_next()
            current.set_next(self.head.get_next())
            self.head = self.head.get_next()
        else:
            current = self.head
            prev = None
            while current.get_next() != self.head:
                prev = current
                current = current.get_next()
                if current == node:
                    prev.set_next(current.get_next())
                    current = current.get_next()

    def josephus_problem(self, step):
        
        current = self.head

        while len(self) > 1:
            count = 1
            while count != step:
                current = current.get_next()
                count +=1 
            self.remove_node(current)

            current = current.get_next()

    def is_circular_linked_list(self, l_list):

        current = l_list.head
        while current.get_next():
            current = current.get_next()
            if current.get_next() == l_list.head:
                return True
            
        return False

if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.append('a')
    cll.append('b')
    cll.append('c')
    cll.append('d')
    print(cll.is_circular_linked_list(cll))
    cll.print_list()
    