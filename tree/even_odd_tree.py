'''
1609 even odd tree
'''
#%%
class tree_node:
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right
root = tree_node(1)
root.left = tree_node(10)
root.right = tree_node(4)
root.left.left = tree_node(3)
root.left.left.left = tree_node(12)
root.left.left.right = tree_node(8)
root.right.left = tree_node(7)
root.right.right = tree_node(9)
root.right.left.left = tree_node(6)
root.right.right.right = tree_node(2)

from collections import deque
class Solutions:
    def even_odd_tree(self, root):
        q = deque()
        q.append(root)
        even = -1
        while q:
            q_len = len(q)
            level = []
            even *= -1
            for i in range(q_len):
                node = q.popleft()
                if node:
                    if even == 1 and node.val%2 == 0:
                        return False
                    if even == 1 and level and node.val < max(level):
                        return False
                    if even == -1 and node.val%2 != 0:
                        return False
                    if even == -1 and level and node.val > min(level):
                        return False  
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
        return True
                    
sln = Solutions()
sln.even_odd_tree(root)
# %%
