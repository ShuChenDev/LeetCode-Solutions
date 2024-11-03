"""
9/20/2024
Set
"""

class Solution(object):
    def containsDuplicate(self, nums):
        n = set()
        for i in range(len(nums)):
            if nums[i] in n:
                return True
            n.add(nums[i])
        return False
