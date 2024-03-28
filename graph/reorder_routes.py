'''
1466 reorder routes to make all paths lead to the city zero
'''
#%%
class Solutions:
    def min_reorder(self, n, connections):
        edges = {(a,b) for a,b in connections}
        neighbors = {city:[] for city in range(n)}
        visited = set()
        changes = 0
        for a,b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)
        def dfs(city):
            nonlocal edges, neighbors, visited, changes
            for neighbor in neighbors[city]:
                if neighbor in visited:
                    continue
                if (neighbor, city) not in edges:
                    changes += 1
                visited.add(neighbor)
                dfs(neighbor)
        visited.add(0)
        dfs(0)
        return changes
n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
sln = Solutions()
sln.min_reorder(n, connections)
# %%
