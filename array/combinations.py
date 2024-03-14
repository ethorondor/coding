'''
77 combinations
'''
#%%
n = 4
k = 2
class Solutions:
    def combinations(self, n, k):
        res = []
        def backtrack(pos, curr):
            if len(curr) == k:
                res.append(curr.copy())
                return 
            for i in range(pos, n+1):
                curr.append(i)
                backtrack(i+1, curr)
                curr.pop()
        backtrack(1,[])
        return res
sln = Solutions()
sln.combinations(n,k)
# %%
