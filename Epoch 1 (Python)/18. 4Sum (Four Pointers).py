"""
10/9/2024
Four Pointers
"""

class Solution(object):
    def fourSum(self, nums, target):
        if len(nums) < 4:
            return []

        nums.sort()
        
        rtn = []
        
        i = 0

        while i < len(nums) - 3:
            j = i + 1
            while j < len(nums) - 2:
                k = j + 1
                l = len(nums) - 1
                
                t = target - nums[i] - nums[j]
                
                while k < l:
                    if nums[k] + nums[l] < t:
                        k += 1
                    elif nums[k] + nums[l] > t:
                        l -= 1
                    else:
                        rtn.append([nums[i], nums[j], nums[k], nums[l]])
                        k+=1
                        l-=1
                        while k < len(nums) and nums[k] == nums[k-1]:
                            k += 1
                        while l > j and nums[l] == nums[l+1]:
                            l -= 1


                j += 1
                while j < len(nums) - 1 and nums[j] == nums[j - 1]:
                    j += 1
            i += 1
            while i < len(nums) - 3 and nums[i] == nums[i - 1]:
                i += 1

        return rtn
