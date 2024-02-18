'''
1 two sum
'''
#%%
nums = [1,2,4,6,8]
target = 12
class solutions:
    def two_sum(self, nums, target):
        hash_map = {}
        for ind, num in enumerate(nums):
            diff = target - num
            if diff in hash_map:
                return [ind, hash_map[diff]]
            hash_map[num] = ind
sln = solutions()
sln.two_sum(nums, target)
# %%
