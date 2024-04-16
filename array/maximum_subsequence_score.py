'''
2542 maximum subsequence score
'''
#%%
import heapq
class Solutions:
    def max_score(self, nums1, nums2, k):
        pairs = [(n1,n2) for n1,n2 in zip(nums1, nums2)]
        pairs.sort(key=lambda x:x[1], reverse=True)
        min_heap = []
        n1_sum = 0
        res = 0
        for n1, n2 in pairs:
            n1_sum += n1
            heapq.heappush(min_heap, n1)
            if len(min_heap) > k:
                n1_pop = heapq.heappop(min_heap)
                n1_sum -= n1_pop
            if len(min_heap) == k:
                res = max(res, n1_sum*n2)
        return res
nums1 = [4,3,3,2] 
nums2 = [2,1,3,4]
k = 3
sln = Solutions()
sln.max_score(nums1, nums2, k)
# %%
