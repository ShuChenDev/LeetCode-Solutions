"""
10/25/2024
Recursion
"""

class Solution(object):
    def isSameTree(self, p, q):
        
        def solve(l, r):
            if not l and not r:
                return True
            
            if not l or not r:
                return False

            if l.val != r.val:
                return False            
            
            return solve(l.left, r.left) and solve(l.right, r.right)

        return solve(p, q)
