'''
1431 kids with greatest number of candies
'''
#%%
candies = [2,3,5,1,3]
extra_candies = 3
class Solutions:
    def greast_candies(self, candies, extra_candies):
        max_candies = max(candies)
        res = []
        for i in candies:
            if i + extra_candies >= max_candies:
                res.append(True)
            else:
                res.append(False)
        return res
sln = Solutions()
sln.greast_candies(candies, extra_candies)
        
# %%
