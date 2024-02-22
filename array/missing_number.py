'''
268 missing number
'''
#%%
nums = [3,0,1]
class solution:
    def missing_number(self, nums):
        res = len(nums)
        for i in range(len(nums)):
            res += (i-nums[i])
        return res
sln = solution()
sln.missing_number(nums)
# %%
