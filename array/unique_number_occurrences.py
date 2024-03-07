'''
1207 unique number of occurrences
'''
#%%
arr = [1,2,2,1,1,3]
class Solutions:
    def unique_occurence(self, arr):
        hash_map = {}
        res = []
        for n in arr:
            if n not in hash_map:
                hash_map[n] = 0
            hash_map[n] += 1
        for i in hash_map.values():
            if i in res:
                return False
            res.append(i)
        return True
sln = Solutions()
sln.unique_occurence(arr)
# %%
