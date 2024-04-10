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
class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        avg = sum(nums[:k])/k
        ans = avg
        for i in range(k, len(nums)):
            avg = (avg*k-nums[i-k]+nums[i])/k
            ans = max(ans, avg)
        return ans
#nums = [7,4,5,8,8,3,9,8,7,6]
nums = [1,12,-5,-6,50,3]
k = 4
sln = Solution()
sln.findMaxAverage(nums, k)
# %%
