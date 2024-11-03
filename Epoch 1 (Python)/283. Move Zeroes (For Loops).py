"""
9/25/2024
For Loop
"""

class Solution(object):
    def moveZeroes(self, nums):        
        start = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.remove(0)
                nums.append(0)
