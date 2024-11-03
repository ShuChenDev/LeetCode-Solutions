"""
9/24/2024
Mathematical
"""

class Solution(object):
    def isUgly(self, n):
        
        if n > 0:
            while(n > 1):
                if n % 2 == 0:
                    n = n / 2
                elif n % 3 == 0:
                    n = n / 3
                elif n % 5 == 0:
                    n = n / 5
                else:
                    return False
            return True
        return False
