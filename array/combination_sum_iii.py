'''
216 combination sum iii
'''
#%%
class Solutions:
    def combination_sum_iii(self, k, n):
        output = []
        def dfs(stack, pos):
            if len(stack) == k:
                if sum(stack) == n:
                    output.append(stack)
                return
            for i in range(pos, 9+1):
                if sum(stack) + i > n:
                    break
                dfs(stack+[i], i+1)
        dfs([],1)
        return output
sln = Solutions()
sln.combination_sum_iii(k=3, n=7)
# %%
