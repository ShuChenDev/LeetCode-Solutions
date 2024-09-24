"""
9/24/2024
XOR
"""

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) == len(t):
            asc = 0
            u = 0
            sMap = {}
            for i in range(len(s)):
                u ^= ord(s[i])
                u ^= ord(t[i])
                asc += ord(s[i])
                asc -= ord(t[i])
                if s[i] in sMap:
                    sMap[s[i]] += 1
                else:
                    sMap[s[i]] = 1

            for i in range(len(t)):
                if t[i] not in sMap:
                    return False
                else:
                    sMap[t[i]] -= 1

            for i in range(len(t)):
                if sMap[t[i]] != 0:
                    return False

            return u == 0 and asc == 0
        return False
