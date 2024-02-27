'''
695 max area of island
'''
#%%
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]
class Solutions:
    def max_area_of_island(self, grid):
        ROW, COL = len(grid), len(grid[0])
        visited = set()
        def dfs(r,c):
            # define all cases when not area counted
            if (r < 0 or r == ROW or c < 0 or c == COL or (r,c) in visited or grid[r][c] == 0):
                return 0
            visited.add((r,c))
            return (1 + dfs(r+1,c) +
                        dfs(r-1,c) +
                        dfs(r,c+1) +
                        dfs(r,c-1))
        area = 0 
        for r in range(ROW):
            for c in range(COL):
                area = max(area, dfs(r,c))
        return area
sln = Solutions()
sln.max_area_of_island(grid)
                   
# %%
