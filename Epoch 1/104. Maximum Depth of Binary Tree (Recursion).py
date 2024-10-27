"""
10/27/2024
Recursion
"""

class Solution(object):
    def maxDepth(self, root):
                
        def solve(tree, i):
            if not tree:
                return i
            return max(solve(tree.left, i+1), solve(tree.right, i+1))

        return solve(root, 0)
