'''
1004 max consecutive ones III
'''
#%%
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
class Solutions:
    def max_ones(self, nums, k):
        l, max_cons = 0, 0
        for r, num in enumerate(nums):
            if num == 0:
                k -= 1
            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
            else:
                max_cons = max(max_cons, r-l+1)
        return max_cons
sln = Solutions()
sln.max_ones(nums, k)
# %%
