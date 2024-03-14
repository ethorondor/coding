'''
252 meeting room
'''
#%%
# definition of intervals
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
i1 = Interval(start=0, end=30)
i2 = Interval(start=5, end=10)
i3 = Interval(start=15, end=20)
intervals = [i1,i2,i3]
class Solutions:
    def meeting_room(self, intervals):
        intervals.sort(key = lambda x:x.start)
        for i in range(1, len(intervals)):
            last = intervals[i-1]
            curr = intervals[i]
            
            if last.end > curr.start:
                return False
        return True
sln = Solutions()
sln.meeting_room(intervals)
# %%
