"""
9/11/2024
Binary Search
"""

class Solution(object):
    def mySqrt(self, x):

        if x == 0 or x == 1:
            return x

        s = 0
        l = x

        while s <= l:
            m = (s + l) // 2
            if m * m > x:
                l = m - 1    
            elif (m) * (m) == x:
                return m
            else:
                s = m + 1

        return l
