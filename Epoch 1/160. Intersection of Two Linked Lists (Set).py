"""
9/17.2024
Set
"""

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        visited = set()
        while headA:
            visited.add(headA)
            headA = headA.next
        while headB:
            if headB in visited:
                return headB
            headB = headB.next

        return headB
