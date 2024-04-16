'''
199 binary tree right side view
'''
#%%
import collections
class tree_node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
root = tree_node(1)
root.left = tree_node(2)
root.right = tree_node(3)
root.left.left = tree_node(6)
root.left.right = tree_node(5)
root.right.left = tree_node(7)
root.right.right = tree_node(4)
class solutions:
    def right_side_view(self, root):
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            q_len = len(q)
            right_node = None
            for i in range(q_len):
                # since we loop through q_len, only the right most node at each level is append to res
                node = q.popleft()
                if node:
                    right_node = node
                    q.append(node.left)
                    q.append(node.right)
            if right_node:
                res.append(right_node.value)
        return res
sln = solutions()
sln.right_side_view(root=root)
# %%
from collections import deque
class Solutions:
    def right_side_view(self, root):
        if not root:
            return None
        res = []
        q = deque()
        q.append(root)
        while q:
            q_len = len(q)
            right_node = None
            for i in range(q_len):
                node = q.popleft()
                if node:
                    right_node = node 
                    q.append(node.left)
                    q.append(node.right)
            if right_node:
                res.append(right_node.val)
        return res
class tree_node:
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right
root = tree_node(1)
root.left = tree_node(2)
root.right = tree_node(3)
root.left.left = tree_node(6)
root.left.right = tree_node(5)
root.right.left = tree_node(7)
root.right.right = tree_node(4)
sln = Solutions()
sln.right_side_view(root)
# %%
print('hello')
# %%
1+3
# %%
