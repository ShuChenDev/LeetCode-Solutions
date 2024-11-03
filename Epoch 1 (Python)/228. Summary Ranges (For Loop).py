"""
9/21/2024
For Loop
"""

class Solution(object):
    def summaryRanges(self, nums):
        if len(nums) > 1:
            rtn = []
            temp = nums[0]

            for i in range(len(nums) - 1):
                if nums[i] + 1 != nums[i + 1]:
                    if nums[i] != temp:
                        rtn.append(str(temp) + '->' + str(nums[i]))
                    else:
                        rtn.append(str(temp))
                    temp = nums[i + 1]
            if nums[-1] - 1 == nums[-2]:
                rtn.append(str(temp) + '->' + str(nums[-1]))
            else:
                rtn.append(str(temp))
            return rtn
        elif len(nums) == 1:
            return [str(nums[0])]
        return []
