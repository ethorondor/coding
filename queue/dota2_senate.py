'''
649 dota2 senate
'''
#%%
from collections import deque
class Solutions:
    def dota(self, senate):
        senate = list(senate)
        D,R = deque(),deque()
        for i,c in enumerate(senate):
            if c == 'R':
                R.append(i)
            else:
                D.append(i)
        while R and D:
            d = D.popleft()
            r = R.popleft()
            if r < d:
                R.append(d+len(senate))
            else:
                D.append(r+len(senate))
        if R:
            return 'R'
        else:
            return 'D'
senate = "RDD"
sln = Solutions()
sln.dota(senate)
# %%
