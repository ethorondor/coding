'''
257 binary tree paths
'''
#%%
class tree_node:
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right
root = tree_node(1)
root.left = tree_node(2)
root.left.left = tree_node(5)
root.right = tree_node(3)

class Solutions:
    def tree_paths(self, root):
        all_path=[]
        curr_path = []
        def dfs(root, curr_path, all_path):
            if not root:
                return None
            curr_path.append(root.val)            
            if not root.left and not root.right:
                all_path.append(curr_path.copy())

            if root.left:
                dfs(root.left, curr_path, all_path)
            if root.right:
                dfs(root.right, curr_path, all_path)
            curr_path.pop()
        dfs(root, curr_path, all_path)
        return all_path
    
sln = Solutions()
sln.tree_paths(root)
            
# %%
