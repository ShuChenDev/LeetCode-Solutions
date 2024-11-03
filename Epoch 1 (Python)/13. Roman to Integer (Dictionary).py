"""
9/3/2024
Dictionary
"""

class Solution(object):
    def romanToInt(self, s):
        dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

        k = len(s)

        sum = dic[s[0]]
        for i in range(1, k):
            if dic[s[i]] > dic[s[i - 1]]:
                sum -= 2* dic[s[i - 1]]
            sum += dic[s[i]]

        return sum
