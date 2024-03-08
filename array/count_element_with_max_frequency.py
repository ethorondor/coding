'''
3005 count elements with maximum frequency
'''
#%%
nums = [1,2,5,3,6,1]
from collections import defaultdict
class Solutions:
    def count_elements(self, nums):
        max_freq = 0
        count = 0
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
            if counts[num] > max_freq:
                max_freq = counts[num]
                count = 1
            elif counts[num] == max_freq:
                count += 1
        return count*max_freq
    
    def count_max_freq_elem(self, nums):
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 0
            freq[n] += 1
        max_freq = max(freq.values())
        res = 0
        for key in freq:
            if freq[key] == max_freq:
                res += freq[key]
        return res
sln = Solutions()
sln.count_max_freq_elem(nums)
# %%
