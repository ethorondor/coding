'''
1071 greatest common divisor of strings
'''
#%%
str1 = 'ABCABC'
str2 = 'ABC'
class Solutions:
    def greatest_common_divisor(self, str1, str2):
        len1, len2 = len(str1), len(str2)
        
        # define a helper function
        def is_divisor(l):
            if len1%l or len2%l:
                return False
            f1 = len1//l
            f2 = len2//l
            return str1[:l]*f1 == str1 and str1[:l]*f2==str2
        for l in range(min(len1,len2), 0 ,-1):
            if is_divisor(l):
                return str1[:l]
        return ''
sln = Solutions()
sln.greatest_common_divisor(str1, str2)
# %%
