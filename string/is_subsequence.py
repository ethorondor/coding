'''
392 is subsequence
'''
#%%
s = 'axc'
t = 'ahbgdc'
class Solutions:
    def is_subsequence(self, s, t):
        c = 0
        i = 0
        while i < len(s) and c < len(t):
            if s[i] == t[c]:
                i += 1
                c += 1
            elif s[i] != t[c]:
                c += 1
        if i == len(s):
            return True
        elif c == len(t):
            return False
sln = Solutions()
sln.is_subsequence(s,t)
# %%
