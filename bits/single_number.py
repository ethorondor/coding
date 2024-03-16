'''
136 sigle number
'''
#%%
nums = [2,2,1]
class Solutions:
    def single_number(self, nums):
        res = 0
        for n in nums:
            res = n^res
        return res
sln = Solutions()
sln.single_number(nums)
# %%
