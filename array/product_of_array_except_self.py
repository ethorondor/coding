'''
238 product of array except self
note: use prix and surfix
'''
#%%
nums = [1,2,3,4]
class Solutions:
    def array_product(self, nums):
        prefix = [0]*len(nums)
        prod = 1
        for i in range(len(nums)):
            if i == 0:
                prod *= 1
                prefix[i] = prod
            else:
                prod *= nums[i-1]
                prefix[i] = prod
        prod = 1
        surfix = [0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                prod *= 1
                surfix[i] = prod
            else:
                prod *= nums[i+1]
                surfix[i] = prod
        res = []
        for i in range(len(nums)):
            res.append(prefix[i]*surfix[i])
        return res
sln = Solutions()
sln.array_product(nums)
# %%
for i in range(4,0,-1):
    print(i)
# %%
