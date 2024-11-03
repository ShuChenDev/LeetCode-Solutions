"""
9/29/2924
Two Pointers with Padding char
"""

class Solution(object):
    def longestPalindrome(self, s):
        if len(s) <= 0:
            return None

        rtn = s[0]
        s = ' ' + s + '|'
        for i in range(len(s)):
            left, right = i, i
            start = True
            while left >= 0 and right < len(s) - 1:
                if start:
                    if s[right + 1] == s[i]:
                        right += 1
                    elif right - left + 1 > len(rtn):
                        rtn = s[left:right+1]
                        start = False
                    else:
                        start = False
                else:
                    if s[right + 1] == s[left - 1]: ##
                        right += 1
                        left -= 1
                    elif right - left + 1 > len(rtn):
                        rtn = s[left:right+1]
                        break
                    else:
                        break
        return rtn
