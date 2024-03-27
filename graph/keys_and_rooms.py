'''
841 keys and rooms
'''
#%%
class Solutions:
    def visit_rooms(self, rooms):
        visited = set()
        stack = [0]
        while stack:
            room = stack.pop()
            if room not in visited:
                visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    stack.append(key)
        return (len(visited) == len(rooms))
rooms = [[1,3],[3,0,1],[2],[0]]
sln = Solutions()
sln.visit_rooms(rooms)
# %%
