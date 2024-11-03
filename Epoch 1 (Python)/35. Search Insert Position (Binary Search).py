"""
9/10/2024
Binary Search
"""
class Solution(object):
    def searchInsert(self, nums, target):
        f = 0
        l = len(nums) - 1

        while f <= l:
            m = (f + l) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                f = m + 1
            else:
                l = m - 1
        return f
