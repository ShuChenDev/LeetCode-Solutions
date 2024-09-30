"""
9/30/2024
2d Array Pointer
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        graph = [[''] for i in range(numRows)]
        y = 0
        down = True
        for i in s:
            graph[y].append(i)
            if y == numRows-1:
                down = False
            elif y == 0:
                down = True

            if down:
                y += 1
            else:
                y -= 1

        return ''.join([''.join(row) for row in graph])
