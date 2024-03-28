'''
1926 nearest exit from entrance in maze
'''
#%%
class Solutions:
    def nearest_exit(self, maze, entrance):
        queue = [(entrance[0],entrance[1])]
        visited = set((entrance[0],entrance[1]))
        steps = 0
        while queue:
            next_queue = []
            for x,y in queue:
                for dx, dy in (0,1),(0,-1),(1,0),(-1,0):
                    nx = x + dx
                    ny = y + dy
                    if not (0<=nx<len(maze) and 0<= ny < len(maze[0])):
                        if (x,y) != (entrance[0],entrance[1]):
                            return steps
                        continue
                    if (nx, ny) in visited:
                        continue
                    if maze[nx][ny] == '+':
                        continue
                    visited.add((nx,ny))
                    next_queue.append((nx,ny))
            queue = next_queue
            steps += 1
        return -1
maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
entrance = [1,2]
sln = Solutions()
sln.nearest_exit(maze, entrance)
# %%
