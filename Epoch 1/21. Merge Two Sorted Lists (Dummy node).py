"""
9/7/2024
Dummy node
"""
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        rtn = ListNode()
        temp = rtn
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        if list1:
            temp.next = list1
        if list2:
            temp.next = list2

        return rtn.next
            