'''
102 binary tree level order traversal
'''
#%%
import collections
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
class solutions:
    def level_order_traversal(self, root):
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            q_len = len(q)
            level = []
            for i in range(q_len):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res
sln = solutions()
sln.level_order_traversal(root=root)
# %%
