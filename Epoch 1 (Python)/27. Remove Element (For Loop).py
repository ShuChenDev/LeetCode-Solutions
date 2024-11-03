"""
9/8/2024
For Loop
"""

class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        while True:
            if k < len(nums):
                if nums[k] == val:
                    del nums[k]
                else:
                    k += 1
            else:
                break

        return k
