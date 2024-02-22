'''
104 maximum depth of a binary tree
'''
#%%
class node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
root = node(6)
root.left = node(2)
root.right = node(8)
root.left.left = node(0)
root.left.right = node(4)
root.right.left = node(7)
root.right.right = node(9)

class Solutions:
    def max_depth(self, root):
        if not root:
            return 0
        return (1 + max(self.max_depth(root.left), self.max_depth(root.right)))
sln = Solutions()
sln.max_depth(root=root)
# %%
