'''
572 subtree of another tree
'''
#%%
class tree_node:
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right
root_1 = tree_node(3)
root_1.left = tree_node(4)
root_1.right = tree_node(5)
root_1.left.left = tree_node(1)
root_1.left.right = tree_node(2)
root_2 = tree_node(4)
root_2.left=tree_node(1)
root_2.right = tree_node(2)

class Solutions:
    def is_subtree(self, s,t):
        if not t:
            return True
        if not s and t:
            return False
        if self.same_tree(s,t):
            return True
        return (self.is_subtree(s.left,t) or self.is_subtree(s.right,t))
        
    def same_tree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return (self.same_tree(s.left, t.left) and self.same_tree(s.right, t.right))
        return False
sln = Solutions()
sln.is_subtree(root_1, root_2)
# %%
