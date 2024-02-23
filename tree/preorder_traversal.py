'''
144 binary tree preorder traversal
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
class solutions:
    def preorder_recursive(self, root):
        res = []
        def preorder(root):
            if not root:
                return None
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return res
    
    def preorder_iterative(self, root):
        curr, stack, res = root, [], []
        while curr or stack:
            if curr:
                res.append(curr.val)
                stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()
        return res
sln = solutions()
sln.preorder_iterative(root=root)
# %%
