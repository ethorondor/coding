'''
700 search in a binary search tree
'''
#%%
class tree_node:
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right
root = tree_node(8)
root.left = tree_node(5)
root.right = tree_node(12)
root.left.left = tree_node(2)
root.left.right = tree_node(6)
root.right.left = tree_node(11)
root.right.right = tree_node(13)
class Solutions:
    def search_binary_tree(self, root, val):
        curr = root
        while curr:
            if val < curr.val:
                curr = curr.left
            elif val > curr.val:
                curr = curr.right
            else:
                return curr
        return None
sln = Solutions()
r = sln.search_binary_tree(root=root, val = 2)
# %%
