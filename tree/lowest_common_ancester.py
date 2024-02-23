'''
235 lowest common ancester of a binary search tree
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
p = node(4)
q = node(0)    

class Solutions:
    def common_ancester(self, root, p, q):
        curr = root
        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr
sln = Solutions()
sln.common_ancester(root, p, q)
# %%
