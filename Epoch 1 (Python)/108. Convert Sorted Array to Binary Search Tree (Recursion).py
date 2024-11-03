"""
10/28/2024
Recursion
"""

class Solution(object):
    def sortedArrayToBST(self, nums):
        

        def solve(nl):
            if not nl:
                return None

            mid = len(nl) // 2
            res = TreeNode(nl[mid])
            res.left = solve(nl[:mid])
            res.right = solve(nl[mid+1:])
            return res


        return solve(nums)
