"""
9/28/2024
Two Pointers and Dictionary
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        rtn = 0

        left = 0
        right = 0

        sSet = set()

        while right < len(s):
            while s[right] in sSet:
                sSet.remove(s[left])
                left += 1
            
            sSet.add(s[right])
            rtn = max(rtn, right - left + 1)
            right += 1

        return rtn
