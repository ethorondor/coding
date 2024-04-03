#%%
class Solutions:
    def reverse_words(self, s):
        word_list = []
        word = ''
        for i in range(len(s)):
            if s[i] == ' ':
                if len(word) > 0:
                    word_list.append(word)
                word = ''
            if s[i] != ' ':
                word += s[i]
        if len(word) > 0:
            word_list.append(word)
        reversed = []
        for i in range(len(word_list)-1, -1, -1):
            reversed.append(word_list[i])
        return ' '.join(reversed)
s = '   the sky is blue  '
sln = Solutions()
sln.reverse_words(s)
# %%
