'''
39 combination sum
see note
'''
#%%
candidates = [2,3,6,7]
target = 7
class Solutions:
    def combination_sum(self, candidates, target):
        dp = [[] for _ in range(target+1)]
        for c in candidates:
            for i in range(1,target+1):
                if i < c: continue
                if i == c:
                    dp[i].append([c])
                else:
                    for blist in dp[i-c]:
                        dp[i].append(blist+[c])
        return dp[target]
sln = Solutions()
sln.combination_sum(candidates, target)
# %%
