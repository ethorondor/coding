'''
450 delete node in bst
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
class Solutions:
    def delete_node(self, root, key):
        if not root:
            return root 
        if key > root.val:
            root.right = self.delete_node(root.right, key)
        elif key < root.val:
            root.left = self.delete_node(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
        # find the min from the right subtree
        curr = root.right
        while curr.left:
            curr = curr.left
        root.val = curr.val
        root.right = self.delete_node(root.right, root.val)
        return root
sln = Solutions()
sln.delete_node(root, 4)
# %%
