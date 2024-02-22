'''
20 valid parenthese
'''
#%%
class Solutions:
    def valid_parenthese(self, s):
        stack = []
        close_to_open = {')':'(',
                         ']':'[',
                         '}':'{'}
        for c in s:
            if c in close_to_open:
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False
                stack.append(c)
            return not stack
s = '((()))[[[]]]'
sln = Solutions()
sln.valid_parenthese(s)
                    
# %%
