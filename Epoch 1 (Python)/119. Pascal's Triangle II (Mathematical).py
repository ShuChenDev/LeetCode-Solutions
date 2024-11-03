"""
9/12/2024
Mathematical
"""

class Solution(object):
    def getRow(self, rowIndex):
        rtn = [1]
        for i in range(rowIndex):
            for j in range(i):
                rtn[j] += rtn[j+1]
            rtn = [1] + rtn
        return rtn
