'''
287 find duplicate number
'''
#%%
nums = [4,5,3,5,2,1]
class solutions:
    def find_duplicate(self, nums):
        slow, fast = 0,0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break 
        slow_2 = 0
        while True:
            slow_2 = nums[slow_2]
            slow = nums[slow]
            if slow == slow_2:
                return slow
sln = solutions()
sln.find_duplicate(nums)

# %%
