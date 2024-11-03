"""
10/16/2024
Binary Search and Two Pointers
"""

class Solution(object):
    def searchRange(self, nums, target):
        
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]


        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid
                right = mid
                while left >= 0 and nums[left] == target:
                    left -= 1

                while right < len(nums) and nums[right] == target:
                    right += 1

                return [left + 1, right - 1]

        return [-1, -1]
