'''
786 kth smallest prime fraction
'''
#%%
import heapq
class Solution:
    def kthSmallestPrimeFraction(self, arr, k):
        heap = []
        heapq.heapify(heap)
        hash_table = {}
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                heapq.heappush(heap, arr[i]/arr[j])
                hash_table[arr[i]/arr[j]] = [arr[i],arr[j]]
        for i in range(k):
            n = heapq.heappop(heap)
        return hash_table[n]
arr = [1,2,3,5]
k = 3
sln = Solution()
sln.kthSmallestPrimeFraction(arr, k)
# %%
