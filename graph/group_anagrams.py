'''
49 group anagrams
'''
#%%
from collections import defaultdict
strs = ["eat","tea","tan","ate","nat","bat"]
class Solutions:
    def group_anagrams(self, strs):
        res = defaultdict(list)
        for s in strs:
            cnt = [0]*26
            for c in s:
                cnt[ord(c)-ord('a')] += 1
            res[tuple(cnt)].append(s)
        return res.values()
sln = Solutions()
sln.group_anagrams(strs)
# %%
