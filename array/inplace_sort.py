'''
inplace sorting
'''
#%%
def inplace_sorting(arr):
    for i in range(len(arr)):
        min_n = arr[i]
        min_i = i
        for j in range(i+1, len(arr)):
            if arr[j] <= min_n:
                min_n = arr[j]
                min_i = j
        arr[i],arr[min_i] = min_n, arr[i]
    return arr
arr = [3,1,6,0,9]
inplace_sorting(arr)
# %%
