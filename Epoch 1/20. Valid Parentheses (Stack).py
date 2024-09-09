"""
9/7/2024
Stack
"""

class Solution(object):
    def isValid(self, s):
        x = len(s)
        if x % 2 == 1 or x == 0:
            return False
        else:
            pairs = {'(':')', '[':']', '{':'}'}
            stack = []
            for i in s:
                if i in pairs: #open bracket
                    stack.append(i)
                elif len(stack) == 0 or i != pairs[stack.pop()]: #closing bracket
                    return False
            return len(stack) == 0
