'''
1046 last stone weight
'''
#%%
import heapq
class solutions:
    def last_stone(self, stones):
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first-second)
        heapq.heappush(stones, 0)
        return -1*stones[0]
stones = [2,7,4,1,8,1]
sln = solutions()
sln.last_stone(stones)
# %%
