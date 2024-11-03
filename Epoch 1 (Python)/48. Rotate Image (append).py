"""
10/24/2024
Append
"""

class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n):
            row = []
            for j in range(n):
                row.append(matrix[j][i])
            for k in range(n//2):
                temp = row[k]
                row[k] = row[-k-1]
                row[-k-1] = temp
            matrix.append(row)

        for i in range(n):
            matrix[i] = matrix.pop(n)
