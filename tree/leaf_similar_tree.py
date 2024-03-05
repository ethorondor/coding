'''
872 leaf similar tree
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
    def dfs(root, res):
        if not root.left and not root.right:
            res.append(root.val)
        if root.left:
            dfs(root.left, res)
        if root.right:
            dfs(root.right, res)
    def get_leaf(root):
        res = []
        dfs(root, res)
        return res
    res1 = get_leaf(root1)
    res2 = get_leaf(root2)
    return res1 == res2
sln = Solutions()
sln.leaf_similar_tree(root=root)
# %%
