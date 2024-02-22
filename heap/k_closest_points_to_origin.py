'''
973 k closest points to origin
'''
#%%
points = [[1,3],[-2,2],[2,3]]
k = 2
import heapq
class solutions:
    def k_closest_point(self, points, k):
        min_heap = []
        for x, y in points:
            dist = (x**2)+(y**2)
            min_heap.append([dist, x, y])
        heapq.heapify(min_heap)
        res = []
        for i in range(k):
            dist, x, y = heapq.heappop(min_heap)
            res.append([x,y])
        return res
sln = solutions()
sln.k_closest_point(points=points, k=k)
# %%
