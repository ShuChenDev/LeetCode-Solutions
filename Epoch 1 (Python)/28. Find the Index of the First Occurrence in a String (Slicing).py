"""
9/9/2024
Slicing
""""

class Solution(object):
    def strStr(self, haystack, needle):
        l = len(needle)
        if l != 0:
            for i in range(len(haystack) - l + 1):
                if haystack[i] == needle[0]:
                    if haystack[i:(i + l)] == needle:
                        return i
        return -1
