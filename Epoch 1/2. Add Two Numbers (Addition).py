"""
9/27/2024
Addition
"""

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        rtn = dummy
        total = 0
        carry = 0

        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
 
            carry = total // 10
            dummy.next = ListNode(total % 10)
            dummy = dummy.next

        return rtn.next
