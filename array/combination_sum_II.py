'''
40 combination sum II
this is based on all subset40
'''
#%%
candidates = [10,1,2,7,6,1,5]
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
    def combination_sum_ii_0(self, candidates, target):
        candidates.sort()
        res = []
        def backtrack_0(pos, curr):
            for i in range(pos, len(candidates)):
                curr.append(candidates[i])
                if curr not in res and sum(curr)==target:
                    res.append(curr.copy())
                backtrack_0(i+1, curr)
                curr.pop()
        backtrack_0(0,[])
        return res
sln = Solutions()
sln.combination_sum_ii_0(candidates, target)
# %%
