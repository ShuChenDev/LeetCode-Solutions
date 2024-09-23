"""
9/22/2024
Stack
"""

class MyQueue(object):

    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)
        

    def pop(self):
        if len(self.stack) > 0:
            rtn = self.stack[0]
            del self.stack[0]
            return rtn
        return -1
        

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[0]
        return -1

    def empty(self):
        return len(self.stack) == 0
