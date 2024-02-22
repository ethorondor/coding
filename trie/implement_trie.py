'''
208 implement trie
'''
#%%
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end_of_word = True
    def search(self, word):
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.end_of_word
    def start_with(self, prefix):
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
trie = Trie()
trie.insert('apple')
trie.search('apple')
trie.start_with('app')
# %%
