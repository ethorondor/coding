'''
994 rotting oranges
'''
#%%
from collections import deque
class Solutions:
    def rotting_oranges(self, grid):
        q = deque()
        time, fresh = 0,0
        R, C = len(grid), len(grid[0])
        for r in range(R):
            for c in range(C):
                if grid[r][c] ==1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])
        directions = [[0,1],[0,-1],[-1,0],[1,0]]
        while q and fresh > 0:
            l_q = len(q)
            for i in range(l_q):
                r,c = q.popleft()
                for dr, dc in directions:
                    row, col = r+dr,c+dc
                    if (row < 0 or col < 0 or row == R or col == C or grid[row][col]!=1):
                        continue
                    grid[row][col] = 2
                    q.append([row,col])
                    fresh -= 1
            time += 1
        return time if fresh ==0 else -1
grid = [[2,1,1],[1,1,0],[0,1,1]]
sln = Solutions()
sln.rotting_oranges(grid)
# %%
