'''
399 evaluation division
'''
#%%
from collections import defaultdict, deque
class Solutions:
    def evaluate_division(self, equations, values, queries):
        adj = defaultdict(list)
        for i , eq in enumerate(equations):
            a,b = eq
            adj[a].append([b, values[i]])
            adj[b].append([a, 1/values[i]])
        def dfs(src, target):
            if src not in adj or target not in adj:
                return -1
            q, visit = deque(), set()
            q.append([src, 1])
            visit.add(src)
            while q:
                n, w = q.popleft()
                if n == target:
                    return w
                for nei, weight in adj[n]:
                    if nei not in visit:
                        q.append([nei, w*weight])
                        visit.add(nei)
            return -1
        return [dfs(q[0],q[1]) for q in queries]
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
sln = Solutions()
sln.evaluate_division(equations=equations, values=values, queries=queries)
# %%
