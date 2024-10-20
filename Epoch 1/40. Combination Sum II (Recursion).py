"""
10/20/2024
Recursion
"""

class Solution(object):
    def combinationSum2(self, candidates, target):
        
        rtn = []
        candidates.sort()
        def solve(i, total, ans):
            if total == target:
                rtn.append(ans[:])
                return

            if i >= len(candidates):
                return
            
            if total >= target:
                return
            
            ans.append(candidates[i])
            solve(i+1, total + candidates[i], ans)
            
            ans.pop()
            
            while i < len(candidates) - 1 and candidates[i] == candidates[i+1]:
                i += 1

            solve(i + 1, total, ans)

            return rtn

        return solve(0, 0, [])
