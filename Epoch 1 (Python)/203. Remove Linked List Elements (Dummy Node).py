'''
9/20/2024
Dummy Node
'''

class Solution(object):
    def removeElements(self, head, val):

        rtn = ListNode()

        rtn.next = head
        temp = rtn

        while temp.next:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return rtn.next
