'''
11 container with most water
'''
#%%
height = [1,8,6,2,5,4,8,3,7]
class Solutions:
    def most_water(self, height):
        l,r = 0,len(height)-1
        res = 0
        while l < r:
            area = (r-l)*min(height[l],height[r])
            res = max(res, area)
            if height[l] < height[r]:
                l +=1
            else:
                r -= 1
        return res
sln = Solutions()
sln.most_water(height)
# %%
