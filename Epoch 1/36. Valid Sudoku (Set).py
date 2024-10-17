"""
10/17/2024
Set
"""

class Solution(object):
    def isValidSudoku(self, board):        
        for i in range(9):
            s1 = set()
            s2 = set()
            s3 = set()
            for j in range(9):

                row = (i // 3) * 3 + (j // 3)
                col = (i % 3) * 3 + (j % 3)
                
                if board[row][col] != ".":
                    if board[row][col] in s3:
                        return False
                    s3.add(board[row][col])

                if board[i][j] != ".":
                    if board[i][j] in s1:
                        return False
                    s1.add(board[i][j])

                if board[j][i] != ".":
                    if board[j][i] in s2:
                        return False
                    s2.add(board[j][i])


        return True
