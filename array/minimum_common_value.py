'''
2540 minimum common value
note: the question is simple, but pay attention to the edge case, when there is no common value, return -1
'''
nums1 = [2,3,4]
nums2 = [2,4]
import numpy as np
class Solutions:
    def min_common_value(self, nums1, nums2):
        set_1, set_2 = set(nums1), set(nums2)
        res = np.inf
        for i in range(max(len(nums1),len(nums2))):
            while i < len(nums1):
                if nums1[i] in set_1 and nums1[i] in set_2:
                    res = min(res, nums1[i])
            while i < len(nums2):
                if nums2[i] in set_1 and nums2[i] in set_2:
                    res = min(res, nums2[i])
        if res == np.inf:
            res = -1
        return res
    