'''
1493 longest subarray of 1s after deleting one element
'''
#%%
nums = [0,1,1,1,0,1,1,0,1]
class Solutions:
    def longest_subarray(self, nums):
        res = 0
        zeros = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1
            while zeros > 1:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            res = max(res, r-l)
        return res     
            

sln = Solutions()
sln.longest_subarray(nums)
# %%
