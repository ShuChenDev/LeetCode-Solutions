"""
9/2/2024
For Loop
"""

class Solution(object):
    def isPalindrome(self, x):
        s = str(x)
        num = len(s)
        
        for i in range(num):
            if s[i] != s[num - i - 1]:
                return False
            
        return True