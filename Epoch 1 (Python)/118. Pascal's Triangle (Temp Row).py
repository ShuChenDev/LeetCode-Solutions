"""
9/11/2024
Temp Row
"""

class Solution(object):
    def generate(self, numRows):
        rtn = [[1]]       
        for i in range(1, numRows):
            row = []
            temp = [0] + rtn[i - 1] + [0]
            for j in range(len(rtn[i - 1]) + 1):
                row.append(temp[j] + temp[j + 1])
            rtn.append(row)
        return rtn
