'''
121 best time to buy and sell stock
'''
#%%
prices = [7,1,5,3,6,4]
class solutions:
    def best_to_buy(self, prices):
        l, r = 0,1
        max_p = 0
        while r < len(prices):
            if prices[l]<prices[r]:
                max_p = max(max_p, prices[r]-prices[l])
            else:
                l = r
            r += 1
        return max_p
sln = solutions()
sln.best_to_buy(prices)
# %%
