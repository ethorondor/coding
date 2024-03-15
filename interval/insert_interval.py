'''
57 insert interval
'''
#%%
intervals = [[1,3],[6,9]]
new_interval = [2,5]
class Solutions:
    def insert_interval(self, intervals, new_interval):
        res = []
        for i in range(len(intervals)):
            if new_interval[1] < intervals[i][0]:
                res.append(new_interval)
                return res + intervals[i:]
            elif new_interval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                new_interval = [min(new_interval[0],intervals[1][0]),max(new_interval[1],intervals[i][1])]
        res.append(new_interval)
        return res
sln = Solutions()
sln.insert_interval(intervals, new_interval)
# %%
09132021