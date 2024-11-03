"""
9/19/2024
ASCII
"""

class Solution(object):
    def titleToNumber(self, columnTitle):
        rtn = 0
        for i in range(len(columnTitle)):
            rtn = 26 * rtn + (ord(columnTitle[i]) - 64)
        return rtn
