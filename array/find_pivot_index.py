'''
724 find pivot index
'''
#%%
nums = [-1,-1,-1,-1,-1,0]
class Solutions:
    def pivot_index(self, nums):
        for i in range(len(nums)):
            if i == 0:
                if sum(nums[1:]) == 0:
                    return i
            if i < len(nums)-1: 
                if sum(nums[:i]) == sum(nums[i+1:]):
                    return i 
            if i == len(nums) -1:
                if sum(nums[:len(nums)-1]) == 0:
                    return i
        return -1
sln = Solutions()
sln.pivot_index(nums)
# %%
