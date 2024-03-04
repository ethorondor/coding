'''
79 word search
'''
#%%
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
class Solutions:
    def word_search(self, board, word):
        path = set()
        ROW, COL = len(board), len(board[0])
        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or
                c < 0 or 
                r >= ROW or
                c >= COL or
                board[r][c] != word[i] or
                (r,c) in path):
                return False
            path.add((r,c))
            res = (dfs(r+1,c,i+1) or 
                    dfs(r-1,c,i+1) or
                    dfs(r,c+1,i+1) or
                    dfs(r,c-1,i+1)
                )
            path.remove((r,c))
            return res
        for r in range(ROW):
            for c in range(COL):
                if dfs(r,c,0):
                    return True
        return False
sln=Solutions()
sln.word_search(board, word)
            
# %%
