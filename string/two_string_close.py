'''
1657 determine if two strings are close
'''
#%%
class Solutions:
    def close_strings(self, word1, word2):
        c1 = {}
        c2 = {}
        for i in range(len(word1)):
            if word1[i] not in c1:
                c1[word1[i]] = 0
            c1[word1[i]] +=1
        for i in range(len(word2)):
            if word2[i] not in c2:
                c2[word2[i]] = 0
            c2[word2[i]] += 1
        n1 = []
        n2 = []
        for _ in c1.values():
            n1.append(_)
        for _ in c2.values():
            n2.append(_)
        n1.sort()
        n2.sort()
        return c1 == c2 or (n1==n2 and set(word1)==set(word2))
word1 = "aa"
word2 = "aaa"
sln = Solutions()
sln.close_strings(word1, word2)
# %%
