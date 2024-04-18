'''
463 island perimeter
'''
#%%
class Solutions:
    def find_perimeter(self, grid):
        R = len(grid)
        C = len(grid[0])
        ans = [0]
        visited = set()
        def count_sides(r,c):
            if r < 0 or r >= R or c < 0 or c >= C:
                return
            if r+1 >= R or grid[r+1][c] == 0:
                ans[0] += 1
            if r-1 < 0 or grid[r-1][c] ==0:
                ans[0] += 1
            if c+1 >= C or grid[r][c+1] == 0:
                ans[0] += 1
            if c-1 < 0 or grid[r][c-1] == 0:
                ans[0] += 1
        def dfs(r,c):
            if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] == 0 or (r,c) in visited:
                return 
            else:
                visited.add((r,c))
                count_sides(r,c)
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
        for r in range(R):
            for c in range(C):
                dfs(r,c)
        return ans[0]
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
sln = Solutions()
sln.find_perimeter(grid)
            
# %%
