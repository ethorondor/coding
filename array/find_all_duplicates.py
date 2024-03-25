'''
442 find all duplicates in an array
'''
nums = [4,3,2,7,8,2,3,1]
class Solutions:
    def find_duplicates(self, nums):
        min_num = nums[0]
        for i in range(nums):
            for j in range(i+1, len(nums)):
                if nums[j] <= nums[i]:
                    