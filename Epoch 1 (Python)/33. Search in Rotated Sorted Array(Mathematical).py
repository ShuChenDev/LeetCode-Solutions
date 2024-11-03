"""
10/12/2024
Mathematical
"""

class Solution(object):
    def search(self, nums, target):
        
        if target < nums[0]:
            i = 0
            while i < len(nums):
                if nums[-(i+1)] > target:
                    i += 1
                elif nums[-(i+1)] == target:
                    return len(nums) - i - 1
                else:
                    return -1
        else:
            i = 0
            while i < len(nums):
                if nums[i] < target:
                    i += 1
                elif nums[i] == target:
                    return i
                else:
                    return -1
        return -1
