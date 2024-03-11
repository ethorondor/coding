'''
347 top k frequent elements
'''
#%%
nums = [4,1,-1,2,-1,2,3]
k = 2
import heapq
class Solutions:
    def top_k_freq(self, nums, k):
        hash_set = {}
        for n in nums:
            if n not in hash_set:
                hash_set[n] = 0
            hash_set[n] += 1
        h = []
        for key,values in hash_set.items():
            heapq.heappush(h, [-values,key])
        res = [heapq.heappop(h)[1] for i in range(k)]
        return res
sln = Solutions()
sln.top_k_freq(nums,k)
# %%
