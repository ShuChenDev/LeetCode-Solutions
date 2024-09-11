"""
9/11/2024
Insert and Merge
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = 0
        j = 0
        while i < m and j < n:
            if nums2[0] <= nums1[i]:
                nums1.insert(i, nums2[0])
                del nums2[0]
                m += 1
                j += 1
            else:
                i += 1

        nums1[m:] = nums2
