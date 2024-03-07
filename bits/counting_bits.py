'''
338 counting bits
'''
#%%
n = 5
class Solutions:
    def count_bits(self, n):
        dp = [0]*(n+1)
        offset = 1
        for i in range(1,n+1):
            if offset * 2 == i:
                offset = i 
            dp[i] = 1 + dp[i-offset]
        return dp
sln = Solutions()
sln.count_bits(n=5)

# %%
