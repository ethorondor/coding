'''
74 search a 2D matrix
'''
#%%
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
class Solutions:
    def search_matrix(self, matrix, target):
        R, C = len(matrix), len(matrix[0])
        t,b = 0, R-1
        while t <= b:
            m_r = (t+b)//2
            if target > matrix[m_r][-1]:
                t = m_r + 1
            elif target < matrix[m_r][0]:
                b = m_r - 1
            else:
                break 
            
        row = (t+b)//2
        l,r = 0,C-1
        while l<=r:
            m = (l+r)//2
            if target > matrix[row][m]:
                l = m+1
            elif target < matrix[row][m]:
                r = m-1
            else:
                return True
        return False
sln = Solutions()
sln.search_matrix(matrix, target)
# %%
