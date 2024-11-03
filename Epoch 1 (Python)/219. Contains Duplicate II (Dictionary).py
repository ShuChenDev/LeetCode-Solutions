"""
9/21/2024
Dictionary
"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        num = {}
        
        for i in range(len(nums)):
            if nums[i] in num:
                for j in range(len(num[nums[i]])):
                    if i - num[nums[i]][j] <= k:
                        return True
                    num[nums[i]].append(i)
            else:
                num[nums[i]] = [i]
        
        return False
        
