"""
10/2/2024
Casting
"""

class Solution(object):
    def myAtoi(self, s):

        s = s.strip()
        rtn = 0
        sign = False
        neg = False

        for i in s:
            if i >= '0' and i <= '9':
                rtn = rtn * 10 + int(i)
                sign = True
            elif i == '+' and not sign:
                sign = True
            elif i == '-' and not sign:
                sign = True
                neg = True
            else:
                break

        if neg:
            rtn = rtn * -1
        if rtn > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif rtn < -2 ** 31:
            return -2 ** 31
        else:
            return rtn
