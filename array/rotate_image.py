'''
48 rotate image
'''
#%%
class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i,len(matrix)):
                _tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = _tmp
        for i in range(len(matrix)):
            l,r = 0,len(matrix)-1
            while l<=r:
                _tmp = matrix[i][l]
                matrix[i][l] = matrix[i][r]
                matrix[i][r] = _tmp
                l += 1
                r -= 1
        return matrix
matrix = [[1,2,3],[4,5,6],[7,8,9]]
sln = Solution()
sln.rotate(matrix)
# %%
