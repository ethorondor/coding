'''
621 task scheduler
'''
#%%
from collections import Counter, deque
import heapq
tasks = ['A','A','A','B','B','B']
#tasks = ["A","C","A","B","D","B"]
n = 2
class Solutions:
    def least_interval(self, tasks, n):
        count = {}
        for task in tasks:
            if task not in count:
                count[task] = 0
            count[task] += 1
        #count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)
        time = 0
        q = deque()
        while max_heap or q:
            time += 1
            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    q.append([cnt, time+n])
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        return time
sln = Solutions()
sln.least_interval(tasks, n)
# %%
