from typing import List
from statistics import median

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        arr = self.mergeArray(nums1,nums2)
        return median(arr)

    def mergeArray(self, nums1: List[int], nums2: List[int]):
        ret = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                ret.append(nums1[i])
                i += 1
            else:
                ret.append(nums2[j])
                j += 1

        while i < len(nums1):
            ret.append(nums1[i])
            i += 1
        while j < len(nums2):
            ret.append(nums2[j])
            j += 1

        return ret
