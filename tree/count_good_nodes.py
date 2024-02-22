'''
1448 count good nodes in binary tree
'''
#%%
class tree_node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
root = tree_node(3)
root.left = tree_node(1)
root.left.left = tree_node(3)
root.right = tree_node(4)
root.right.left = tree_node(1)
root.right.right = tree_node(5)

class solutions:
    def count_good_node(self, root):
        max_val = root.value
        def dfs(node, max_val):
            if not node:
                return 0
            if node.value >= max_val:
                res = 1
            else:
                res = 0
            max_val = max(node.value, max_val)
            res += dfs(node.left, max_val)
            res += dfs(node.right, max_val)
            return res 
        return dfs(root, max_val)
sln = solutions()
sln.count_good_node(root)
# %%
