'''
9 palindrome number
'''
#%%
x = -121
class solutions:
    def is_palindrome(self, nums):
        l ,r = 0, len(str(nums))-1
        while l <= r:
            if str(nums)[l] != str(nums)[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
    
sln = solutions()
sln.is_palindrome(nums = x)
# %%
