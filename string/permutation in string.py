"""
567 permutation in string
"""
#%%
from collections import defaultdict
class Solutions:
    def permutation_string(self, s1, s2):
        s1_dict = defaultdict(int)
        s2_dict = defaultdict(int)
        s = 'abcdefghijklmnopqrstuvwxyz'
        for c in s:
            s1_dict[c] = 0
            s2_dict[c] = 0
        l1 = len(s1)
        l2 = len(s2)
        for c in s1:
            s1_dict[c] += 1
        for i in range(l1):
            s2_dict[s2[i]] += 1
        if s1_dict == s2_dict:
            return True     
        for i in range(l1,l2):
            s2_dict[s2[i-l1]] -= 1
            s2_dict[s2[i]] += 1
            if s1_dict == s2_dict:
                return True 
        return False
s1 = "abc"
s2 = 'qdcab'
sln = Solutions()
sln.permutation_string(s1, s2)
# %%
