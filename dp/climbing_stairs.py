'''
75 climbing stairs
'''
#%%
n = 5
class Solutions:
    def climb_stairs(self, n):
        last_one, last_two = 1,1
        for i in range(n-1):
            tmp = last_one
            last_one = last_one + last_two
            last_two = tmp
        return last_one
sln = Solutions()
sln.climb_stairs(n)
# %%
