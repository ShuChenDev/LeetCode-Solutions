"""
9/18/2024
ASCII
"""

class Solution(object):
    def convertToTitle(self, columnNumber):

        rtn = ''
        while columnNumber > 0:
            if columnNumber % 26 == 0 and columnNumber != 0:
                rtn = 'Z' + rtn
                columnNumber -= 1
            else:
                rtn = chr(columnNumber % 26 + 64) + rtn
            columnNumber = columnNumber // 26 
            
        return rtn
