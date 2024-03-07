'''
1679 max number of k-sum pairs
'''
#%%
nums = [1,2,3,4]
k = 5
import collections
class Solutions:
    def max_operations(self, nums, k):
        hash_map = {}
        operations = 0
        for n in nums:
            diff = k-n
            if diff not in hash_map:
                hash_map[diff] = 0
            if n not in hash_map:
                hash_map[n] = 0
            if hash_map[diff] > 0:
                operations += 1
                hash_map[diff] -= 1
            else:
                hash_map[n] += 1
        return operations
sln = Solutions()
sln.max_operations(nums, k)            
# %%
