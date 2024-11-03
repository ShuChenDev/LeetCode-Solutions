"""
10/7/2024
Four Pointers
"""

class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        
        pad = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r', 's'], '8':['t','u','v'], '9':['w','x','y','z']}
        rtn = []
        i = 0
        j = 0
        k = 0
        l = 0

        while i < len(pad[digits[0]]):
            row = pad[digits[0]][i]


            if len(digits) > 1:
                row = row + pad[digits[1]][j]
                if len(digits) > 2:
                    row = row + pad[digits[2]][k]
                    if len(digits) > 3:
                        row = row + pad[digits[3]][l]
                        
            rtn.append(row)
            
            if len(digits) > 3:
                l += 1
                if l == len(pad[digits[3]]):
                    l = 0
                    k += 1
                    if k == len(pad[digits[2]]):
                        k = 0
                        j += 1
                        if j == len(pad[digits[1]]):
                            j = 0
                            i += 1
            elif len(digits) == 3 and (len(digits) <= 3 or l == 0):
                k += 1
                if k == len(pad[digits[2]]):
                    k = 0
                    j += 1
                    if j == len(pad[digits[1]]):
                        j = 0
                        i += 1
            elif len(digits) == 2 and (len(digits) <= 2 or (k == 0 and l == 0)):
                j += 1
                if j == len(pad[digits[1]]):
                    j = 0
                    i += 1

            if len(digits) == 1:
                i += 1
                
        return rtn
