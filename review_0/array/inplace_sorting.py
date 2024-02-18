'''
inplace sorting
'''
#%%
nums = [3,1,6,0,9]
class solutions:
    def inplace_sorting(self, nums):
        for i in range(len(nums)):
            curr_min = nums[i]
            min_index = i
            for j in range(i+1, len(nums)):
                if nums[j] < curr_min:
                    min_index = j
                    curr_min = nums[j]
            nums[i], nums[min_index] = curr_min, nums[i]
        return nums      
sln = solutions()
sln.inplace_sorting(nums)              
# %%
