"""
10/29/2024
Recursion
"""

class Solution(object):
    def inorderTraversal(self, root):
        
        def solve(ans, l):
            if l is None:
                return

            solve(ans, l.left)            
            ans.append(l.val)
            solve(ans, l.right)            

        rtn = []
        solve(rtn, root)
        return rtn
