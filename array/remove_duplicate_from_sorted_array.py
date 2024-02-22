'''
26 remove duplicate from sorted array
'''
#%%
nums = [1,1,4,4,5,5]
class Solutions:
    def remove_duplicate(self, nums):
        l = 0
        r = 1
        while r < len(nums):
            if nums[l] == nums[r]:
                nums.pop(r)
            else:
                l+=1
                r+=1
        return len(nums)
sln = Solutions()
sln.remove_duplicate(nums)
# %%
