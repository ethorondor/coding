'''
98 validate binary search tree
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
    def is_valid_bst(self, root):
        def valid(root, left, right):
            if not root:
                return True
            if not (root.val > left and root.val < right):
                return False
            return (valid(root.left, left, root.val) and 
                    valid(root.right, root.val, right))
        return valid(root, float('-inf'), float('inf'))
sln = Solutions()
sln.is_valid_bst(root)  
# %%
