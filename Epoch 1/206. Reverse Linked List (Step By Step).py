"""
9/20/2024
Step By Step
"""

class Solution(object):
    def reverseList(self, head):

        end = None

        while head:
            temp = head.next
            head.next = end
            end = head
            head = temp

        return end
