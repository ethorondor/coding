'''
100 same tree
'''
#%%
class tree_node:
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right
r1 = tree_node(1)
r1.left = tree_node(2)
r1.right = tree_node(3)
r2 = tree_node(1)
r2.left = tree_node(2)
r2.right = tree_node(3)

class Solutions:
    def same_tree(self, r1, r2):
        if not r1 and not r2:
            return True
        elif not r1 and r2:
            return False
        elif r1 and not r2:
            return False
        elif r1.val != r2.val:
            return False
        return (self.same_tree(r1.left,r2.left) and self.same_tree(r1.right, r2.right))
sln = Solutions()
sln.same_tree(r1, r2)
# %%
