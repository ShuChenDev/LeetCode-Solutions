"""
9/16/2024
Fast Slow Pointers
"""

class Solution(object):
    def hasCycle(self, head):
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            head = head.next 
            if fast == head:
                return True
        return False
