'''
643 maximum average subarray I
'''
#%%
nums = [1,12,-5,-6,50,3]
class solutions:
    def maximum_average(self, nums, k):
        _sum = 0
        for i in range(k):
            _sum += nums[i]
        max_avg = _sum/k
        for i in range(k, len(nums)):
            _sum = _sum - nums[i-k] + nums[i]
            max_avg = max(max_avg, _sum/k)
        return max_avg
sln = solutions()
sln.maximum_average(nums=nums, k=2)
            
# %%
