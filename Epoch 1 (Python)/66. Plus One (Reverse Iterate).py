"""
9/10/2024
Reverse Iterate
"""

class Solution(object):
    def plusOne(self, digits):
        if digits[len(digits) - 1] != 9:
            digits[len(digits) - 1] += 1
            return digits
        else:
            for i in range(len(digits) - 1, -1, -1):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    return digits

            for i in range(len(digits)):
                digits[i] = 0
            return [1] + digits
