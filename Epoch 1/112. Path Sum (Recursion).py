"""
11/1/2024
Recursion
"""

class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        def solve(l, ans):
            ans = ans + l.val

            if not l.left and not l.right:
                return ans == targetSum

            lleaf = False
            rleaf = False
            if l.left:
                lleaf = solve(l.left, ans)
            if l.right:
                rleaf = solve(l.right, ans)

            return lleaf or rleaf
        
        return solve(root, 0)
