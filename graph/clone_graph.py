'''
133 clone graph
'''
#%%
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
        
class Solutions:
    def clone_graph(self, node):
        old_to_new = {}
        def dfs (node):
            if node in old_to_new:
                return old_to_new[node]
            if not node:
                return
            copy = Node(node.val)
            old_to_new[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node)

n1 = Node(1,[2,3])
n2 = Node(2,[1,4])
n3 = Node(3,[1,4])
n4 = Node(4,[2,3])
sln = Solutions()
sln.clone_graph(n1)
# %%
