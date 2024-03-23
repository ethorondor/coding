'''
283 move zeros
'''
#%%
nums = [0,1,0,3,12]
class Solutions:
    def move_zeros(self, nums):
        i = 0
        for c in range(len(nums)):
            if nums[i] == 0:
                _ = nums.pop(i)
                nums.append(_)
            else:
                i += 1
        return nums
sln = Solutions()
sln.move_zeros(nums)
                
# %%
