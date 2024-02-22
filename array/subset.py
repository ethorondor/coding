'''
78 subsets
note: in subsets, order does not matter
'''
#%%
nums = [1,2,3]
class Solutions:
    def subset(self, nums):
        subset = []
        subset.append([])
        for n in nums:
            l = len(subset)
            for i in range(l):
                s = subset[i].copy()
                s.append(n)
                subset.append(s)
        return subset
    
    def subset_1(self, nums):
        res = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            #decision to include nums[i]
            subset.append(nums[i])
            dfs(i+1)
            #decision not to include nums[i]
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res
sln = Solutions()
sln.subset(nums)
# %%
