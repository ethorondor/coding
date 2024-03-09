'''
2352 equal row and column pairs
'''
#%%
grid = [[3,2,1],[1,7,6],[2,7,7]]
import numpy as np
class Solutions:
    def equal_row_column(self, grid):
        arry = np.array(grid)
        cnt = 0
        for i in range(len(grid)):
            for k in range(len(grid)):
                r = arry[i,:]
                c = arry[:,k]
                bool = True
                for j in range(len(r)):
                    if r[j] != c[j]:
                        bool = False
                if bool:
                    cnt += 1
        return cnt
sln = Solutions()
sln.equal_row_column(grid)
# %%
