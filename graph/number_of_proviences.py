'''
547 number of provinces
'''
#%%
class Solutions:
    def number_proviences(self, isConnected):
        def dfs(i):
            visited.add(i)
            for j in range(n):
                if j not in visited and isConnected[i][j] == 1:
                    dfs(j)
        n = len(isConnected)
        visited = set()
        components = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                components += 1
        return components
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
sln = Solutions()
sln.number_proviences(isConnected)
# %%
