'''
215 kth largest element in an array
'''
#%%
nums = [3,2,1,5,6,4]
k = 2
import heapq
class solutions:
    def kth_largest(self, nums, k):
        max_heap = [-1*s for s in nums]
        heapq.heapify(max_heap)
        for i in range(k-1):
            heapq.heappop(max_heap)
        return -1*heapq.heappop(max_heap)
sln = solutions()
sln.kth_largest(nums=nums, k=k)
# %%
