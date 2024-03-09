'''
242 valid anagram
'''
#%%
s = "anagram"
t = "nagaram"
class Solutions:
    def valid_anagram(self, s,t):
        set_s, set_t = {}, {}
        if len(s) != len(t):
            return False 
        for i in range(len(s)):
            if s[i] not in set_s:
                set_s[s[i]] =0
            set_s[s[i]] += 1
            if t[i] not in set_t:
                set_t[t[i]] = 0
            set_t[t[i]] += 1
        return set_s == set_t
sln = Solutions()
sln.valid_anagram(s,t)
# %%
