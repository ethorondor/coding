"""
2962 count subarray where max element appears at least k times
"""
#%%
class Solutions:
    def count_subarray(self, nums, k):
        max_n = nums[0]
        count = 0
        for n in nums:
            max_n = max(max_n, n)
        
        for i in range(len(nums)):
            n_max = 0
            for j in range(i, len(nums)):
                if nums[j] == max_n:
                    n_max +=1
                if n_max >= k:
                    count += 1
        return count

nums = [1,3,2,3,3]
k = 2
sln = Solutions()
sln.count_subarray(nums, k)
# %%
