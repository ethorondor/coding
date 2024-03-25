'''
130 surrounded regions
'''
#%%
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
class Solutions:
    def solve(self, board):
        '''
        do not return anything, modify board in-place instead
        '''
        R, C = len(board), len(board[0])
        visited = set()
        def dfs(r,c):
            if (r < 0 or c < 0 or r == R or c == C or board[r][c] != 'O' or (r,c) in visited):
                return
            visited.add((r,c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        for r in range(R):
            for c in range(C):
                if board[r][c] == 'O' and (r in [0, R-1] or c in [0, C-1]):
                    dfs(r,c)
        for r in range(R):
            for c in range(C):
                if board[r][c] == 'O' and (r,c) not in visited:
                    board[r][c] = 'X'
sln = Solutions()
sln.solve(board)
# %%
