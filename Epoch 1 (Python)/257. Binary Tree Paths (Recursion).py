"""
11/2/2024
Recursion
"""

class Solution(object):
    def binaryTreePaths(self, root):
        
        if not root:
            return ''
        
        def solve(node, ans, rtn):
            if not node:
                return

            if not node.left and not node.right:
                rtn.append(ans + str(node.val))
                return rtn

            ans = ans + str(node.val) + '->'

            solve(node.left, ans , rtn)
            solve(node.right, ans , rtn)

            return rtn
        
        return solve(root, '', [])
