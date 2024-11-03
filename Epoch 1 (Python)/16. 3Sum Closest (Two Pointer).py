"""
10/6/2024
Two Pointer
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        
        nums.sort()
        rtn = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                res = nums[i] + nums[left] + nums[right]

                if abs(target - res) <= abs(target - rtn):
                    rtn = res

                if res < target:
                    left += 1
                elif res > target:
                    right -=1
                else:
                    return res
        
        return rtn
