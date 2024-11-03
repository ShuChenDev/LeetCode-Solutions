"""
10/3/2024
Two Pointers
"""

class Solution(object):
    def maxArea(self, height):

        left = 0
        right = len(height) - 1
        rtn = 0
        
        while left < right:
            rtn = max(rtn, min(height[left], height[right]) * (right - left))
            if height[left] > height[right]:
                right -= 1
            else:
                left +=1
        return rtn
