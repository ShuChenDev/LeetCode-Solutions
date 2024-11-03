"""
11/2/2024
Recursion
"""

class Solution(object):
    def postorderTraversal(self, root):
        
        if not root:
            return []

        def solve(node, ans):
            if not node:
                return ans
            
            ans = solve(node.left, ans)
            ans = solve(node.right, ans)
            ans.append(node.val)
            return ans

        return solve(root, [])
