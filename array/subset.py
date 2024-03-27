'''
78 subsets
note: in subsets, order does not matter
'''
#%%
nums =  [1,2,3]
class Solutions:
    def subset(self, nums):
        nums.sort()
        subset = []
        subset.append([])
        for n in nums:
            l = len(subset)
            for i in range(l):
                s = subset[i]
                subset.append(s+[n])
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
    def subset_backtrack(self,nums):
        res = []
        def backtrack(curr, pos):
            for i in range(pos,len(nums)):
                curr.append(nums[i])
                if curr not in res:
                    res.append(curr.copy())
                backtrack(curr, i+1)
                curr.pop()
        backtrack([],0)
        return res
    def subset_dfs(self,nums):
        nums.sort()
        res = []
        def dfs(stack, pos):
            res.append(stack)
            for i in range(pos, len(nums)):
                dfs(stack+[nums[i]], i+1)
        dfs([], 0)
        return res
sln = Solutions()
sln.subset(nums)
# %%
