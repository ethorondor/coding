'''
713 subarray product less than k
'''
#%%
#%%
class Solutions:
    def subarray_product(self, nums,k):
        res = 0
        product = 1
        l = 0
        for r in range(len(nums)):
            product *= nums[r]
            while l<=r and product >=k:
                product = product//nums[l]
                l += 1
            res += r-l+1
        return res
nums = [10,5,2,6]
k = 150
sln = Solutions()
sln.subarray_product(nums, k)
# %%
