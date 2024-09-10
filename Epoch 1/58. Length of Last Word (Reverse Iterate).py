"""
9/10/2024
Reverse Iterate
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        rtn = 0
        w = False
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                w = True
                rtn += 1
            elif w:
                return rtn

        return rtn
