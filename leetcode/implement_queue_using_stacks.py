"""
https://leetcode.com/problems/implement-queue-using-stacks/description/

"""

class MyQueue:

    def __init__(self):
        self.q = []

    def push(self, x):
        self.q.append(x)

    def pop(self):
        return self.q.pop(0)

    def peek(self):
        return self.q[0]

    def empty(self):
        if len(self.q) > 0:
            return False 
        else:
            return True 
        