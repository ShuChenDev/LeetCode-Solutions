"""
9/26/2024
Dictionary
"""

class Solution(object):
    def wordPattern(self, pattern, s):
        pMap = {}
        sSet = set()
        s = s.split(" ")

        if len(pattern) != len(s):
                return False

        for i in range(len(pattern)):
            if pattern[i] in pMap and pMap[pattern[i]] != s[i]:
                return False
            elif s[i] in sSet and pattern[i] not in pMap:
                return False               
            else:
                pMap[pattern[i]] = s[i]
                sSet.add(s[i])

        return True
