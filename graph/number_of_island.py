'''
200 number of islands
'''
#%%
from collections import deque
grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
grid = [["1","1","1"],["0","1","0"],["1","1","1"]]
import collections
class Solutions:
    def num_islands(self, grid):
        if not grid:
            return 0
        visited = set()
        ROW, COL = len(grid), len(grid[0])
        ans = 0
        def dfs(r,c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                (row, col) = q.popleft()
                directions = [[0,1],[0,-1],[-1,0],[1,0]]
                for (dr,dc) in directions:
                    _r = row+dr
                    _c = col+dc
                    if (_r in range(ROW) and
                        _c in range(COL) and
                        (_r,_c) not in visited and
                        grid[_r][_c] == '1'):
                        q.append((_r,_c))
                        visited.add((_r,_c))
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == '1' and (r,c) not in visited:
                    dfs(r,c)
                    ans+=1
        return ans
    
sln = Solutions()
sln.num_islands(grid)
# %%
