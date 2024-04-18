'''
623 add one row to tree
'''
#%%
class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

class Solution:
    def addOneRow(self, root, val, depth):
        if depth == 2:
            if root.left:
                _tmp = root.left
                root.left = TreeNode(val)
                root.left.left = _tmp
            
            if root.right:
                _tmp = root.right
                root.right = TreeNode(val)
                root.right.right = _tmp
        elif depth > 2:
            if root.left:
                self.addOneRow(root.left,val, depth-1)
            if root.right:
                self.addOneRow(root.right,val, depth-1)
        else:
            return root
        return root
sln = Solution()
r = sln.addOneRow(root, 5, 4)
                
# %%
