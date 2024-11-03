"""
9/24/2024
Mathematicle
"""

class Solution(object):
    def missingNumber(self, nums):
        
        add = 0
        res = 0

        for i in range(len(nums)):
            add += nums[i]
            res += i
        res += len(nums)

        return res - add
