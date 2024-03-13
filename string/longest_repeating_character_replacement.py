'''
424 longest repeating character replacement
'''
#%%
s = 'ABAB'
k = 2
class Solutions:
    def longest_repeating_substring(self, s, k):
        str_count = {}
        res = 0
        l = 0
        for r in range(len(s)):
            str_count[s[r]] = 1+str_count.get(s[r],0)
            if (r-l+1) - max(str_count.values()) > k:
                str_count[s[l]] -= 1
                l+=1
            res = max(res, r-l+1)
        return res
sln = Solutions()
sln.longest_repeating_substring(s,k)
