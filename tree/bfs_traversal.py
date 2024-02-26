'''
bfs traverse a tree, this is the same as lever order traserval
'''
#%%
from collections import deque
class tree_node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
root = tree_node(12)
root.left = tree_node(7)
root.right = tree_node(1)
root.left.left = tree_node(9)
root.right.left = tree_node(10)
root.right.right = tree_node(5)

def bfs(root):
    res = []
    if not root:
        return res
    q = deque()
    q.append(root)
    while q:
        level = []
        q_len = len(q)
        for i in range(q_len):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)
    return res
bfs(root)
# %%
