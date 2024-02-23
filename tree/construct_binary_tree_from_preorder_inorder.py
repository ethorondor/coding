'''
105 construct binary tree from preorder and inorder traversal
'''
#%%
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solutions:
    def build_tree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        # the right sie is not inclusive
        root.left = self.build_tree(preorder[1:mid+1], inorder[:mid])
        root.right = self.build_tree(preorder[mid+1:], inorder[mid+1:])
        return root
sln = Solutions()
sln.build_tree(preorder, inorder)
# %%
