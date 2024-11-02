"""
11/2/2024
Recursion
"""

class Solution(object):
    def countNodes(self, root):

        if not root:
            return 0

        def solve(node, ans):
            if not node:
                return ans
            
            ans = solve(node.left, ans+1)
            ans = solve(node.right, ans+1)
            return ans
        
        return solve(root, 0) // 2
