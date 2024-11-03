"""
9/23/2024
Reverse Half
"""

class Solution(object):
    def isPalindrome(self, head):
        if head:
            mid = head
            end = head
            while end and end.next:
                mid = mid.next
                end = end.next.next

            previous = None
            while mid:
                temp = mid.next
                mid.next = previous
                previous = mid
                mid = temp

            while previous and head:
                if previous.val == head.val:
                    previous = previous.next
                    head = head.next
                else:
                    return False
        return True
