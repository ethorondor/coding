'''
211 design add and search words data structure
'''
#%%
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    
    def add_word(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end_of_word = True
    
    def search(self, word):
        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.childrec[c]
            return cur.end_of_word
        return dfs(0, self.root)
word_dict = WordDictionary()
word_dict.add_word('bad')
word_dict.add_word('dad')
word_dict.search('map')
# %%
