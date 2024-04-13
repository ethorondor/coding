'''
735 asteroid collision
'''
#%%
asteroids = [5,10,-5]
class Solutions:
    def collision(self, asteroids):
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    a = 0
                else:
                    a = 0
                    stack.pop()
            if a:
                stack.append(a)
        return stack
sln = Solutions()
sln.collision(asteroids)
# %%
class Solutions:
    def collision(self, asteroids):
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                b = stack.pop()
                if abs(a) < abs(b):
                    a = b
                elif abs(a) > abs(b):
                    continue
                else:
                    a = 0
            if a:
                stack.append(a)
        return stack

asteroids = [-2,-1,1,2]
sln = Solutions()
sln.collision(asteroids)    
# %%
