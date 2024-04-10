'''
950 reveal cards in increasing order
'''
#%%
from collections import deque
class Solutions:
    def reveal_cards(self, deck):
        res = [0]*len(deck)
        deck.sort()
        q = deque(range(len(deck)))
        for n in deck:
            i = q.popleft()
            res[i] = n
            if q:
                q.append(q.popleft())
        return res
deck = [17,13,11,2,3,5,7]
sln = Solutions()
sln.reveal_cards(deck)
# %%
