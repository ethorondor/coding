'''
94 binary tree inorder traversal
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
    def inorder_traversal_recursive(self, root):
        res = []
        def inorder(root):
            if not root:
                return None
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        return res
    def inorder_traversal_iterative(self, root):
        curr, stack, res = root, [], []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res
sln = solutions()
sln.inorder_traversal_iterative(root)
# %%
