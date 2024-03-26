'''
394 decode string
'''
#%%
class Solutions:
    def decode_str(self, str):
        stack = []
        for i in range(len(str)):
            if str[i] != ']':
                stack.append(str[i])
            else:
                substring = ''
                while stack[-1] != '[':
                    substring += stack.pop()
                stack.pop()
                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k)*substring)
        return ''.join(stack)
s = "3[a]2[bc]"
sln = Solutions()
sln.decode_str(str=s)
# %%
