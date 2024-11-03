"""
9/11/2024
Mathematical
"""

class Solution(object):
    def climbStairs(self, n):
        f = 0
        l = 1
        temp = 0
        for i in range(n):
            temp = l
            l += f
            f = temp

        return l
