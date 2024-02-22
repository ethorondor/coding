'''
find the average of subarray of length k
'''
#%%
nums = [1,3,2,6,8]
k = 2
class solutions:
    def ave_subarray(self, nums, k):
        _sum = 0
        res = []
        for i in range(k):
            _sum += nums[i]
        res.append(_sum/k)
        for i in range(k, len(nums)):
            _sum = _sum - nums[i-k] + nums[i]
            res.append(_sum/k)
        return res 
sln = solutions()
sln.ave_subarray(nums=nums, k=k)
# %%
