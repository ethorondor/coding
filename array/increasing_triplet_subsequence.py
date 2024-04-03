'''
334 increasing triplet subsequence
'''
#%%
import numpy as np
#nums = [1,5,0,4,1,3]
nums = [1,1,-2,7]
class Solutions:
    def increasing_triplet(self, nums):
        n1, n2 = np.inf, np.inf
        for n in nums:
            if (n > n2):
                return True
            if (n <= n1):
                n1 = n
            elif (n <= n2):
                n2 = n
        return False
sln = Solutions()
sln.increasing_triplet(nums)
