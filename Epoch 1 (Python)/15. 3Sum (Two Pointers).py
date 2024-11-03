"""
10/5/2024
Two Pointers
"""

class Solution(object):
    def threeSum(self, nums):
        
        rtn = []

        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
        
            j = i + 1
            k = len(nums) - 1

            while j < k:
                res = nums[i] + nums[j] + nums[k]
                if res < 0:
                    j += 1       
                elif res > 0:
                    k -= 1                
                else:
                    rtn.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1    
        return rtn
