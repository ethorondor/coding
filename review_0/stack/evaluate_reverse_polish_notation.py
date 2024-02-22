'''
150 evaluate reverse polish notation
'''
#%%
tokens = ["2","1","+","3","*"]
class Solutions:
    def evaluate_polish_notation(self, tokens):
        stack = []
        for c in tokens:
            if c == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(a+b)
            elif c == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif c == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(a*b)
            elif c == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(b/a)
            else:
                stack.append(int(c))
        return stack.pop()
sln = Solutions()
sln.evaluate_polish_notation(tokens=tokens)
# %%
