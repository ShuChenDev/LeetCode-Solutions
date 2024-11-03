"""
9/21/2024
While Loop
"""

class Solution(object):
    def isPowerOfTwo(self, n):
        s = 1
        while s <= n:
            if s == n:
                return True
            s *= 2
        return False
