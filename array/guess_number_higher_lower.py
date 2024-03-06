'''
374 guess number higher or lower
'''
#%%
n = 10
class Solutions:
    def guessNumber(self, n):
        l,r = 1,n
        while True:
            m = (l+r)//2
            res = guess(m)
            if res > 0:
                l = m+1
            elif res < 0:
                r = m-1
            else:
                return m