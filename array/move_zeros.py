'''
283 move zeros
'''
#%%
nums = [0,1,0,3,12]
class Solutions:
    def move_zeros(self, nums):
        count = 0
        i = 0
        while count < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                count +=1
            else:
                i +=1
                count +=1
        return nums
sln = Solutions()
sln.move_zeros(nums)
                
# %%
