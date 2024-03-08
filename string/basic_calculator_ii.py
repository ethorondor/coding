'''
227 basic calculator II
'''
#%%
class solutions:
    def basic_calculator(self, s):
        if not s:
            return 0
        stack = []
        curr_num = 0
        operator = '+'
        operators = {'+','-','*','/'}
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                curr_num = curr_num*10+int(c)
            if c in operators or i == len(s)-1:
                if operator == '+':
                    stack.append(curr_num)
                if operator == '-':
                    stack.append(-curr_num)
                if operator == '*':
                    stack[-1] *= curr_num
                if operator == '/':
                    _n = stack.pop()
                    ans = int(_n/curr_num)
                    stack.append(ans)
                curr_num = 0
                operator = c
        return sum(stack)

s = '1+5*3-3/3 '
sln = solutions()
sln.basic_calculator(s)
# %%
