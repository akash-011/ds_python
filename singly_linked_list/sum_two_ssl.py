from singly_linked_list import LinkedList

def sum_two_ssl(ssl1, ssl2):
    p = ssl1.head 
    q = ssl2.head 

    final_list = LinkedList()
    carry = 0 

    while p or q:
        if not p:
            i = 0 
        else:
            i = p.get_data()
        if not q:
            j = 0
        else:
            j = q.get_data()
        s = i + j + carry
        if s >= 10:
            carry = 1
            remainder = s%10
            final_list.append(remainder)
        else:
            final_list.append(s)

        if p:
            p = p.get_next()
        if q:
            q = q.get_next()
    
    return final_list

if __name__ == "__main__":
    ss1 = LinkedList()
    ss1.append(6)
    ss1.append(5)
    ss1.append(3)

    ss2 = LinkedList()
    ss2.append(4)
    ss2.append(8)
    result = sum_two_ssl(ss1,ss2)
    result.print_nodes()
    

