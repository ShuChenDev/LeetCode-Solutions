"""
10/18/2024
Recursion
"""

class Solution(object):
    def countAndSay(self, n):
        def rle(s):
            rle = ''
            c = 1
            for i in range(0, len(s) - 1):
                if s[i] == s[i + 1]:
                    c += 1
                else:
                    rle += str(c) + s[i]
                    c = 1

            rle += str(c) + s[-1]

            return rle

        rtn = '1'
        
        for i in range(n-1):
            rtn = rle(rtn)

        return rtn
