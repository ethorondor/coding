'''
853 car fleet
'''
#%%
target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
class solutins:
    def car_fleet(self, position,speed, target):
        pair = [[p,s] for p,s in zip(position, speed)]
        stack = []
        for p,s in sorted(pair)[::-1]:
            stack.append((target-p)/s)
            if len(stack)>= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
sln = solutins()
sln.car_fleet(position=position, speed=speed, target=target)
# %%
class Solution:
    def carFleet(self, target: int, position, speed) -> int:
        sort_position = []
        for i in range(len(position)):
            sort_position.append([position[i],speed[i]])
        sort_position.sort(key=lambda x:x[0])
        stack = []
        res = 0
        for i in range(len(position)):
            t = (target-sort_position[::-1][i][0])/sort_position[::-1][i][1]
            stack.append(t)
            if len(stack)>=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
target = 12
position = [10,8]
speed = [2,4,1,1,3]
sln = Solution()
sln.carFleet(target, position, speed)
# %%
