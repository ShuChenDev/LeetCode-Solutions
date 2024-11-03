"""
9/20/2024
Dictionary
"""

class Solution(object):
    def isIsomorphic(self, s, t):

        if len(s) == len(t):
            sMap = {}
            tMap = {}

            for i in range(len(s)):
                if s[i] in sMap and sMap[s[i]] != t[i] or t[i] in tMap and tMap[t[i]] != s[i]:
                    return False
                sMap[s[i]] = t[i]            
                tMap[t[i]] = s[i]
            return True

        return False
