"""
10/01/2024
Mathematical
"""

class Solution(object):
    def reverse(self, x):

        rtn = 0
        
        neg = False
        if x < 0:
            x = x*-1
            neg = True
        
        while x>0:
            rtn = rtn * 10 + x % 10
            x = x // 10
        
        if rtn > 2**31 - 1:
            return 0
        elif neg:
            return rtn*-1
        return rtn
