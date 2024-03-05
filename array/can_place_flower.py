'''
605 can place flower
'''
#%%
flowerbed = [0,0]
n = 2
class Solutions:
    def place_flower(self, flowerbed, n):
        ans = 0
        for i in range(len(flowerbed)-1):
            if i == 0 and flowerbed[i] == 0 and flowerbed[i+1]==0:
                flowerbed[i] = 1
                ans += 1
            elif flowerbed[i] == 0:
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    ans += 1
        if flowerbed[len(flowerbed)-2] == 0 and flowerbed[len(flowerbed)-1] == 0:
            ans += 1
        return ans >= n 
sln = Solutions()
sln.place_flower(flowerbed, n)     
# %%
