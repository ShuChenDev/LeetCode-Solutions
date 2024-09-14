"""
9/14/2024
Clean and Compare Reverse
"""

class Solution(object):
    def isPalindrome(self, s):
        temp = []
        for i in s:
            if 'A' <= i <= 'Z':
                temp.append(chr(ord(i) + 32))
            elif 'a' <= i <= 'z' or '0' <= i <= '9':
                temp.append(i)
        c = temp[:]
        c.reverse()
        return c == temp 
