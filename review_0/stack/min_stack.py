'''
155 min stack
design a stack that supports push, pop, top and retrieving the minimum element in constant time.
# note: the key is to keep track of the minimum value while we push and pop
'''
#%%
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, val):
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            min_val = min(val, self.min_stack[-1])
            self.min_stack.append(min_val)
    def pop(self):
        self.stack.pop()
        self.min_stack.pop()
    def top(self):
        return self.stack[-1]
    def get_min(self):
        return self.min_stack[-1]
minstack = MinStack()
minstack.push(-1)
minstack.push(0)
# %%
minstack.pop()
# %%
minstack.get_min()
# %%
