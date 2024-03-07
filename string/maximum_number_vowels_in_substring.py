'''
1456 maximum number of vowels in a substring of given length
'''
#%%
s="ibpbhixfiouhdljnjfflpapptrxgcomvnb"
k = 33
class Solutions:
    def max_vowels(self, s,k):
        vowels = ['a','e','i','o','u']
        cnt = 0
        res = 0
        for i in range(k):
            if s[i] in vowels:
                cnt += 1
        for i in range(0,len(s)-k):
            if s[i] in vowels:
                cnt -= 1
            if s[i+k] in vowels:
                cnt +=1
            res = max(res, cnt)
        return res
sln = Solutions()
sln.max_vowels(s, k)
# %%
