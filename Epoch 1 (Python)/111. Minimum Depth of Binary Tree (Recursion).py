"""
10/31/2024
Recursion
"""

class Solution(object):
    def minDepth(self, root):
   
        if not root:
            return 0

        def solve(l, s):
            if not l:
                return float('inf')
            if not l.left and not l.right:
                return s+1
                
            left=solve(l.left, s+1)
            right=solve(l.right, s+1)

            return min(left, right)

        return solve(root, 0)
