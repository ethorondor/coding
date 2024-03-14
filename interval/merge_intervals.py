'''
56 merge intervals
'''
#%%
intervals = [[1,3],[2,6],[8,10],[15,18]]
class Solutions:
    def merge_intervals(self, intervals):
        intervals.sort(key = lambda x:x[0])
        output = [intervals[0]]
        for left, right in intervals[1:]:
            last_right = output[-1][1]
            if left <= last_right:
                output[-1][1] = max(right, last_right)
            else:
                output.append([left,right])
        return output 
sln = Solutions()
sln.merge_intervals(intervals)
# %%
