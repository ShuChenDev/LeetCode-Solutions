"""
10/21/2024
Two Pointers
"""

class Solution(object):
    def jump(self, nums):
        if len(nums) == 1:
            return 0

        jump = 0
        i = 0

        while i < len(nums) - 1:
            if i + nums[i] >= len(nums) - 1:
                return jump + 1 

            k = nums[i]
            nxt = i + nums[i]

            for j in range(1, nums[i] + 1):
                if i + j < len(nums):
                    if i + j + nums[i + j] > k:
                        k = i + j + nums[i+j]
                        nxt = i + j
            
            if nxt == i:
                break

            i = nxt
            jump += 1

        return jump
