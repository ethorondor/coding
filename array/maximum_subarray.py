'''
53 maximum subarray
whenever the cum sum is less that zero, we can reset, and start with a new subarray
'''
#%%
nums = [-2,-1,-1,-4,-1,-3,-2,-3]
class solusions:
    def max_sum(self, nums):
        max_sum = nums[0]
        curr_sum = 0
        for n in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += n
            max_sum = max(max_sum, curr_sum)
        return max_sum
sln = solusions()
sln.max_sum(nums=nums)
# %%
