"""
https://leetcode.com/problems/swap-nodes-in-pairs

"""
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = next 


def swap_node_pairs(head):
    dummy = prev = ListNode(0)
    prev.next = head 
    while prev.next and prev.next.next:
        a = prev.next 
        b = a.next 
        prev.next , a.next, b.next = b, b.next , a 
        prev = a 

    return dummy.next

