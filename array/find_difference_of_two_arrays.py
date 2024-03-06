'''
2215 find the difference of two arrays
'''
#%%
nums1 = [1,2,3]
nums2 = [2,4,6]
class Solutions:
    def findDifference(self, nums1, nums2):
        nums1_set, nums2_set = set(nums1), set(nums2)
        res1, res2 = set(), set()
        for n in nums1:
            if n not in nums2_set:
                res1.add(n)
        for n in nums2:
            if n not in nums1_set:
                res2.add(n)
        return [list(res1), list(res2)]
sln = Solutions()
sln.findDifference(nums1, nums2)
        
# %%
