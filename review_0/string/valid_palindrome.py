'''
125 valid palindrome
'''
#%%
s = "A man, a plan, a canal: Panama"
class solutions:
    def valid_palindrome(self, s):
        new_str = ''
        for c in s:
            if c.isalnum():
                new_str += c.lower()
        return (new_str == new_str[::-1])
sln = solutions()
sln.valid_palindrome(s)
            
# %%
