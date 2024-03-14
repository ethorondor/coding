'''
435 non-overlap intervals
'''
#%%
intervals = [[1,2],[2,3],[3,4],[1,3]]
class Solutions:
    def nonoverlap_intervals(self, intervals):
        res = 0
        output = [intervals[0]]
        for left, right in intervals[1:]:
            last_right = output[-1][1]
            if last_right>left:
                res += 1
                output[-1][1] = min(right, last_right)
            else:
                output.append([left, right])
        return res
sln = Solutions()
sln.nonoverlap_intervals(intervals)
# %%
