"""
9/4/2024
Sort
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        for i in range(len(strs[0])):
            if strs[0][i] != strs[-1][i]:
                return strs[0][:i]

        if strs[0] != "":
            return strs[0]
        return ""
