'''
55 jump game
'''
#%%
nums = [2,3,1,1,4]
class Solutions:
    def can_jump(self, nums):
        goal = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        if goal == 0:
            return True
        else:
            return False
sln = Solutions()
sln.can_jump(nums)
# %%
