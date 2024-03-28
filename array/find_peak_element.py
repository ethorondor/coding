'''
162 find peak element
'''
#%%
class Solutions:
    def find_peak(self, nums):
        if len(nums)==1:
            return 0
        res = []
        for i in range(0, len(nums)):
            if i == 0:
                if nums[i] > nums[i+1]:
                    res.append(i)
            elif i == len(nums)-1:
                if nums[i] > nums[i-1]:
                    res.append(i)
            elif i >0 and i < len(nums)-1:
                if (nums[i] > nums[i-1]) and (nums[i] > nums[i+1]):
                    res.append(i)
        return res[0]
nums = [1]
sln = Solutions()
sln.find_peak(nums)
# %%
