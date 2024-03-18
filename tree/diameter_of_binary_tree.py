'''
543 diameter of binary tree
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
    def diameter_of_tree(self, root):
        res = [0]
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(res[0], left+right)
            return 1+max(left, right)
        dfs(root)
        return res[0]
sln = Solutions()
sln.diameter_of_tree(root)
# %%
