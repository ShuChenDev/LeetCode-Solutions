"""
10/4/2024
Dictionary
"""

class Solution(object):
    def intToRoman(self, num):
        
        symbol = {1:['I','V'], 2:['X','L'], 3:['C','D'], 4:['M','M']}
        rtn = ''
        digit = 0

        while num > 0:
            i = num % 10
            num = num // 10
            digit += 1

            if i == 4:
                rtn = symbol[digit][0] + symbol[digit][1] + rtn
            elif i == 9:
                rtn = symbol[digit][0] + symbol[digit + 1][0] + rtn
            else:
                rtn = (i %5) * symbol[digit][0] + rtn
                if i >= 5:
                    rtn = symbol[digit][1] + rtn
        return rtn
