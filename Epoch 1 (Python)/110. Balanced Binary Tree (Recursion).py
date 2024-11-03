"""
10/30/2024
Recursion
"""

class Solution(object):
    def isBalanced(self, root):
        if not root:
            return True
        
        def solve(l):
            
            if not l:
                return 0
            return max(solve(l.left), solve(l.right)) + 1
                 
        return abs(solve(root.left) - solve(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
