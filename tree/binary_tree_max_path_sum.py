'''
124 binary tree maximum path sum
'''
#%%
class tree_node:
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right
root = tree_node(1)
root.left = tree_node(2)
root.right = tree_node(3)
root.left.left = tree_node(4)
root.left.right = tree_node(5)
class Solutions:
    def max_path_sum(self, root):
        res = [root.val]
        def dfs(root):
            if not root:
                return 0
            left_max = dfs(root.left)
            right_max = dfs(root.right)
            left_max = max(left_max, 0)
            right_max = max(right_max,0)
            res[0] = max(res[0], left_max+right_max+root.val)
            return root.val + max(right_max, left_max)
        dfs(root)
        return res[0]
sln = Solutions()
sln.max_path_sum(root)
# %%
