'''
226 invert binary tree
'''
#%%
class tree_node:
    def __init__(self, val, left = None, right = None):
        self.value = val
        self.left = left
        self.right = right
root = tree_node(1)
root.left = tree_node(2)
root.right = tree_node(3)
root.left.left = tree_node(4)
root.left.right = tree_node(5)
class Solutions:
    def invert_binary_tree(self, root):
        if not root:
            return None
        _tmp = root.left
        root.left = root.right
        root.right = _tmp
        self.invert_binary_tree(root.left)
        self.invert_binary_tree(root.right)
        return root
sln = Solutions()
sln.invert_binary_tree(root=root)
        
# %%
