'''
112 path sum
'''
#%%
class tree_node:
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right
root = tree_node(5)
root.left = tree_node(4)
root.left.left = tree_node(11)
root.left.left.left = tree_node(7)
root.left.left.right = tree_node(2)
root.right = tree_node(8)
root.right.left = tree_node(13)
root.right.right = tree_node(4)
root.right.right.right = tree_node(1)
class Solutions:
    def path_sum(self, root, target):
        all_path = []
        curr_path = []
        ans = [False]
        def dfs(root, target, curr_path, all_path, ans):
            if ans[0]:
                return
            if not root:
                return None
            curr_path.append(root.val)
            if not root.left and not root.right:
                all_path.append(curr_path.copy())
                ans[0] = (root.val == target)
            else:
                target -= root.val
                if root.left:
                    dfs(root.left, target, curr_path, all_path, ans)
                if root.right:
                    dfs(root.right, target, curr_path, all_path, ans)
            curr_path.pop()
        dfs(root, target, curr_path, all_path, ans)
        return ans[0]

        
sln = Solutions()
sln.path_sum(root,target=22)
# %%
