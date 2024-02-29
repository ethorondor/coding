'''
40 combination sum II
this is based on all subset40
'''
#%%
candidates = [1,2,6,1,5]
target = 8

class Solutions:
    def combination_sum_ii(self, candidates, target):
        candidates.sort()
        res = []
        def backtrack(curr, pos, target):
            if target == 0:
                return res.append(curr.copy())
            if target < 0:
                return
            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                curr.append(candidates[i])
                backtrack(curr, i+1, target-candidates[i])
                curr.pop()
                prev = candidates[i]
        backtrack([], 0, target)
        return res
sln = Solutions()
sln.combination_sum_ii(candidates, target)
# %%
