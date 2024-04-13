'''
236 lowest common ancester
'''
#%%
class Solutions:
    def lowest_common_ancester(self, root, p, q):
        if root.val == p.val or root.val == q.val:
            return root
        if root.left is None and root.right is None:
            return None
        l = None
        r = None
        if root.left:
            l = self.lowest_common_ancester(root.left, p, q)
        if root.right:
            r = self.lowest_common_ancester(root.right, p ,q)
        if l and r:
            return root
        else:
            return l or r
class tree_node:
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right
root = tree_node(3)
root.left = tree_node(5)
root.left.left = tree_node(6)
root.left.right = tree_node(2)
root.left.right.left = tree_node(7)
root.left.right.right = tree_node(4)
root.right = tree_node(1)
root.right.left = tree_node(0)
root.right.right = tree_node(8)
p = 5
q = 1
sln = Solutions()
r = sln.lowest_common_ancester(root, tree_node(p), tree_node(q))
# %%
