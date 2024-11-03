"""
10/10/2024
ListNode
"""

class Solution(object):
    def swapPairs(self, head):

        dummy = ListNode(0, head)
        previous = dummy
        cur = head

        while cur and cur.next:
            left = cur.next.next
            temp = cur.next

            temp.next = cur
            cur.next = left
            previous.next = temp

            previous = cur
            cur = left

        return dummy.next
