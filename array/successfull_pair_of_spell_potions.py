'''
2300 successful pairs of spells and potions
'''
#%%
class Solutions:
    def successful_pairs(self, spells, potions, success):
        potions.sort()
        res = []
        for s in spells:
            idx = len(potions)
            l,r=0,len(potions)-1
            while l <= r:
                m = (l+r)//2
                if s*potions[m] >= success:
                    r = m-1
                    idx = m
                else:
                    l += 1
            res.append(len(potions)-idx)
        return res
spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7
sln = Solutions()
sln.successful_pairs(spells, potions, success)
# %%
