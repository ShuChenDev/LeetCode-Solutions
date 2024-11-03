"""
11/2/2024
Recursion
"""

class Solution(object):
    def preorderTraversal(self, root):
        
        if not root:
            return []

        def solve(node, ans):
            if not node:
                return ans
            
            ans.append(node.val)            
            ans = solve(node.left, ans)
            ans = solve(node.right, ans)
            return ans

        return solve(root, [])
