'''
66 plus one
'''
#%%
digits = [9,9,9]
class Solutions:
    def add_one(self, digits):
        digits = digits[::-1]
        one, i = 1,0
        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
            else:
                digits.append(1)
                one = 0
            i += 1
        return digits[::-1]
sln = Solutions()
sln.add_one(digits)
# %%
d = [1,2,3]
s=0
for i in range(len(d)):
    s = 10*s + d[i]
    
# %%
