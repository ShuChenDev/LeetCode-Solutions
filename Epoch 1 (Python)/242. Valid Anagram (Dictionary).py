"""
9/24/2024
Dictionary
"""

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) == len(t):
            sMap = {}
            for i in range(len(s)):
                if s[i] in sMap:
                    sMap[s[i]] += 1
                else:
                    sMap[s[i]] = 1

            for i in range(len(t)):
                if t[i] not in sMap:
                    return False
                else:
                    sMap[t[i]] -= 1

            for i in range(len(s)):
                if sMap[s[i]] != 0:
                    return False

            return True
        return False
