'''
448 find all numbers disappeared in an array
'''
#%%
class solutions:
    def find_all_missing_numbers(self, nums):
        i = 0
        while i < len(nums):
            j = nums[i]-1
            if nums[i] != nums[j]:
                _tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = _tmp
            else:
                i += 1
        missing = []
        for i in range(len(nums)):
            if nums[i]!=i+1:
                missing.append(i+1)
        return missing
    
    def find_disappear_nums(self, nums):
        for n in nums:
            i = abs(n) -1
            nums[i] = -1 * abs(nums[i])
        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i+1)
        return res
    
nums = [5,4,4,3,5]
s = solutions()
s.find_all_missing_numbers(nums)
# %%
