'''
345 reverse vowels of a string
'''
#%%
s = 'hello'
class Solutions:
    def reverse_vowels(self, s):
        l, r = 0, len(s)-1
        string = [i for i in s]
        vows = ['a','e','i','o', 'u']
        while l <= r:
            if string[l] in vows and string[r] in vows:
                string[l],string[r] = string[r],string[l]
                l += 1
                r -= 1
            elif string[l] in vows and string[r] not in vows:
                r -= 1
            elif string[l] not in vows and string[r] in vows:
                l += 1
            else:
                l += 1
                r -= 1
        return ''.join(string)
sln = Solutions()
s = sln.reverse_vowels(s)
# %%
