'''
133 clone graph
'''
#%%
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.neighbors = [n2,n4]
n3.neighbors = [n2,n4]
n2.neighbors = [n1,n3]
n4.neighbors = [n1,n3]

class Solutions:
    def clone_graph(self, node):
        old_to_new = {}
        def dfs(node):
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
sln = Solutions()
n = sln.clone_graph(n1)
# %%
