'''
1372 longest zigzag path in a binary tree
'''
#%%
class tree_node:
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right
root = tree_node(3)
root.left = tree_node(9)
root.right = tree_node(20)
root.left.left = tree_node(15)
root.left.right = tree_node(7)
class Solutions:
    def longest_zigzag(self, root):        
        def dfs(root, is_left, depth):
            if not root:
                return depth
            if is_left:
                depth = max(depth, 
                            dfs(root.right, False, depth+1),
                            dfs(root.left, True, 0)
                            )
            else:
                depth = max(depth, 
                            dfs(root.left, True, depth+1),
                            dfs(root.right, False, 0)
                            )
            return depth
        return max(dfs(root.left, True, 0), dfs(root.right, False, 0))
sln = Solutions()
sln.longest_zigzag(root)
# %%
