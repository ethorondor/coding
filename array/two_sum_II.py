'''
167 two sum with sorted integers
Note: this problem is solved wit two pointers
'''
#%%
nums = [0,2,3,6,7]
target = 5
class solutions:
    def two_sum_II(self, nums, target):
        l, r = 0, len(nums)-1
        while l <= r:
            _sum = nums[l]+nums[r]
            if _sum < target:
                l += 1
            elif _sum > target:
                r -= 1
            else:
                return [l,r]
sln = solutions()
sln.two_sum_II(nums, target)
# %%
