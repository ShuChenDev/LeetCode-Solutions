"""
9/21/2024
self.stack
"""

class MyStack(object):

    def __init__(self):
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
            return self.stack.pop()
        return -1
        
    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
            return self.stack[-1]
        return -1

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack) == 0
