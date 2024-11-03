"""
9/19/2024
Mathematical
"""

class Solution(object):
    def hammingWeight(self, n):
        rtn = 0
        check = 1
        
        while n > 0:
            if check <= n and check * 2 > n:
                n = n - check
                check = 1
                rtn += 1
            else:
                check = check * 2

        return rtn
