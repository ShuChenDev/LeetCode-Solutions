"""
10/19/2024
Recursion
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        rtn = []
        
        def solve(i, cur, tol):
            if tol == target:
                rtn.append(cur[:])
                return

            if tol > target or i >= len(candidates):
                return

            cur.append(candidates[i])
            solve(i, cur, tol + candidates[i])
            cur.pop()
            solve(i + 1, cur, tol)

            return rtn

        return solve(0, [], 0)
