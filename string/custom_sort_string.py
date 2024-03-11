'''
791 custom sort string
'''
#%%
order = "cba"
s = "dabcd"
class Solutions:
    def custom_sort(self, order, s):
        order_dict = {val:key for key, val in enumerate(order)}
        string = [c for c in s]
        for i in range(len(string)):
            if string[i] in order_dict:
                min_n = order_dict[string[i]]
                min_i = i
            else:
                continue
            for j in range(i+1, len(string)):
                if string[j] in order_dict:
                    if order_dict[string[j]] < min_n:
                        min_n = order_dict[string[j]]
                        min_i = j
            
            string[i], string[min_i] = string[min_i], string[i]                  
        return ''.join(string)
sln = Solutions()
sln.custom_sort(order, s)
# %%
