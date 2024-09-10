"""
9/10/2024
Sync Digit + Reverse Iterate
"""

class Solution(object):
    def addBinary(self, a, b):
        rtn = ''
        carry = 0
        
        l = max(len(a), len(b))
        a = a.zfill(l)
        b = b.zfill(l)
        carry = 0

        for i in range(l - 1, -1, -1):
            d = int(a[i]) + int(b[i]) + carry
            if d < 2:
                rtn = str(d) + rtn
                carry = 0
            else:
                carry = 1         
                if d == 2:
                    rtn = '0' + rtn
                else:
                    rtn = '1' + rtn
        if carry == 1:
            rtn = '1' + rtn
        return rtn
