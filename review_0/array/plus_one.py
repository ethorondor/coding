'''
66 plus one
'''
#%%
digits = [1,2,3]
class Solutions:
    def plus_one(self, digits):
        output = []
        res = 0
        for i in range(len(digits)):
            res += 10**(len(digits)-1-i)*digits[i]
        res += 1
        for i in str(res):
            output.append(int(i))
        return output
sln = Solutions()
sln.plus_one(digits=digits)
# %%
