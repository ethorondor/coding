'''
739 daily temperatures
'''
#%%
temperatures = [73,74,75,71,69,72,76,73]
class Solutions:
    def daily_temp(self, temperatures):
        stack = []
        res = [0]*len(temperatures)
        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                idx, temp = stack.pop()
                res[idx]=i-idx
            stack.append([i,t])
        return res
sln = Solutions()
sln.daily_temp(temperatures)