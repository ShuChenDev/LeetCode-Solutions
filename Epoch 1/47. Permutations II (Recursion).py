"""
10/22/2024
Recursion
"""

class Solution(object):
    def permute(self, nums):
        if len(nums) <= 1:
            return [nums]

        rtn = []

        def solve(cur, ans):
            if len(ans) == len(nums):
                rtn.append(ans)
                return

            for i in range(len(nums)):
                


        solve(nums, [])
        return rtn
