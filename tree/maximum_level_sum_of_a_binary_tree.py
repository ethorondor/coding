'''
1161 maximum level sum of a binary tree
'''
#%%
class tree_node:
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right
root = tree_node(1)
root.left = tree_node(1)
root.right = tree_node(0)
root.left.left = tree_node(7)
root.left.right = tree_node(-8)
root.right.left=tree_node(-7)
root.right.right=tree_node(9)
from collections import deque
class Solutions:
    def max_level_sum(self, root):
        q = deque()
        q.append(root)
        l = 0
        level_max = root.val
        res = 1
        while q:
            q_len = len(q)
            level = []
            l += 1
            for _ in range(q_len):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                if sum(level) > level_max:
                    res = l
                level_max = max(level_max, sum(level))
        return res 
sln = Solutions()
sln.max_level_sum(root)
# %%
