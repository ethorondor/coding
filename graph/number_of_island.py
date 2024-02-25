'''
200 number of islands
'''
#%%
grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
grid = [["1","1","1"],["0","1","0"],["1","1","1"]]
import collections
class Solutions:
    def num_islands(self, grid):
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0
        
        def dfs(r,c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[-1,0]]
                for dr,dc in directions:
                    r,c = row+dr, col+dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == '1' and
                        (r,c) not in visit):
                        q.append((r,c))
                        visit.add((r,c))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visit:
                    dfs(r,c)
                    islands += 1
        return islands
sln = Solutions()
sln.num_islands(grid)
# %%
