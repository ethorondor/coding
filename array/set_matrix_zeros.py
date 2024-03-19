'''
73 set matrix zeros
'''
#%%
class Solutions:
    def set_zeros(self, matrix):
        visited = set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0 and (r,c) not in visited:
                    for i in range(len(matrix)):
                        if (i,c) not in visited and matrix[i][c] != 0:
                            visited.add((i,c))
                        matrix[i][c] = 0
                    for i in range(len(matrix[0])):

                        if (r,i) not in visited and matrix[r][i] != 0:
                            visited.add((r,i))  
                        matrix[r][i] = 0  
        return matrix
matrix = [[1,1,1],[1,0,1],[1,1,1]]
sln = Solutions()
sln.set_zeros(matrix)                
# %%
