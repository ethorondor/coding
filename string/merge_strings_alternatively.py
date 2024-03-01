'''
1768 merge strings alternatively
'''
#%%
word1 = 'abc'
word2 = 'edksf'
class Solutions:
    def merge_strings(self, word1, word2):
        l = min(len(word1), len(word2))
        res = ''
        for i in range(l):
            res += word1[i]
            res += word2[i]
        w1 = word1[i+1:]
        w2 = word2[i+1:]
        if w1:
            res += w1
        if w2:
            res += w2
        return res
sln = Solutions()
sln.merge_strings(word1, word2)
# %%
