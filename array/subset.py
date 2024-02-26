'''
78 subsets
note: in subsets, order does not matter
'''
#%%
nums = [4,4,4,1,4]
class Solutions:
    def subset(self, nums):
        nums.sort()
        subset = []
        subset.append([])
        for n in nums:
            l = len(subset)
            for i in range(l):
                s = subset[i].copy()
                s.append(n)
                if s not in subset:
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
