'''
2390 remove stars from a string
'''
#%%
s = 'leet**cod*e'
class Solutions:
    def remove_star(self, s):
        stack = []
        for c in s:
            if c == '*':
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)
sln = Solutions()
sln.remove_star(s)
# %%
