'''
131 palindrome partitioning
'''
#%%
import copy
s = 'aab'
class Solutions:
    def palindrome_partitioning(self, s):
        res = []
        def is_palindrome(s):
            l ,r = 0, len(s)-1
            while l <= r:
                if s[l] == s[r]:
                    l+=1
                    r-=1
                else:
                    return False
            return True

        for l in range(len(s)):
            for r in range(l+1,len(s)+1):
                substring = s[l:r]
                print(substring)
                if is_palindrome(substring):
                    res.append(substring)
        return res
sln = Solutions()
sln.palindrome_partitioning(s)            

# %%
