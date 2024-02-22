'''
46 permutations
'''
#%%
nums = [1,2,3]
class Solutions:
    def permute(self, nums):
        result = []
        if (len(nums)==1):
            return [nums[:]]
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
        return result
sln = Solutions()
sln.permute(nums)
# %%
