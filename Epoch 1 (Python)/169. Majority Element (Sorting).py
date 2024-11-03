"""
9/19/2024
Sorting
"""

class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]
