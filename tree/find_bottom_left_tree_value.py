'''
513 find bottom left tree value
note: this is a variant question of level order traversal
'''
#%%
from collections import deque
class tree_node:
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right
root = tree_node(3)
root.left = tree_node(9)
root.right = tree_node(20)
root.left.left = tree_node(15)
root.left.right = tree_node(7)

class Solutions:
    def bottom_left_value(self, root):
        res = []
        q = deque()
        q.append(root)
        while q:
            level = []
            q_len = len(q)
            for i in range(q_len):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res[-1][0]
sln = Solutions()
sln.bottom_left_value(root)
# %%
