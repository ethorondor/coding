'''
207 course schedule
'''
#%%
prereq = [[0,1],[0,2],[1,3],[1,4],[3,4]]
prerequisites = [[1,0]]
class Solutions:
    def can_finish(self, num_course, prerequisites):
        pre_map = {i:[] for i in range(num_course)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)
        
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if pre_map[crs] == []:
                return True
            visited.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            pre_map[crs] = []
            return True
        for crs in range(num_course):
            if not dfs(crs):
                return False 
        return True
sln = Solutions()
sln.can_finish(2, prerequisites)
# %%
