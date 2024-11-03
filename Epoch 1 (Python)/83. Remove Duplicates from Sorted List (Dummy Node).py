"""
9/11/2024
Dummy Node
"""

class Solution(object):
    def deleteDuplicates(self, head):
    
        rtn = ListNode()
        temp = rtn

        while head:
            if head.next and head.val == head.next.val:
                head = head.next
            else:
                temp.next = head
                temp = temp.next
                head = head.next
        temp.next = None
        return rtn.next
