"""
10/13/2024
Two Pointers
"""

class Solution(object):
    def removeNthFromEnd(self, head, n):        
        temp = ListNode()
        dummy = temp.next

        if not head.next:
            return dummy
        if not head.next.next:
            if n == 1:
                head.next = dummy
            else:
                head = head.next

            return head

        right = head
        left = temp
        left.next = head

        i = 0

        while right:
            right = right.next
            i += 1
            if i > n:
                left = left.next
        left.next = left.next.next

        if i <= n:
            return head.next
        
        return head
