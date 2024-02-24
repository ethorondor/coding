'''
145 postorder traversal
'''
#%%
class tree_node:
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right
root = tree_node(5)
root.left = tree_node(1)
root.right = tree_node(7)
root.right.left = tree_node(6)
root.right.right = tree_node(8)

class Solutions:
    def postorder_traversal(self, root):
        res = []
        def postorder(root):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)
        postorder(root)
        return res
sln = Solutions()
sln.postorder_traversal(root)
# %%
