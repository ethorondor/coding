'''
202 happy number
'''
#%%
n = 19
class Solutions:
    def is_happy(self, n):
        visited = set()
        def square_sum(n):
            if n == 1:
                return True
            if n in visited:
                return False
            visited.add(n)
            sums = 0
            for n in str(n):
                sums += int(n)*int(n)
            return square_sum(sums)
        return square_sum(n)
sln = Solutions()
b = sln.is_happy(19)
# %%
