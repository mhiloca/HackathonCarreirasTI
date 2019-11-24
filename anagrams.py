from collections import Counter
from itertools import combinations


class Anagram:

    def __init__(self, w):
        self.w = self.phrase(w)


    def phrase(self, w):

        alph = 'ABCDEFGHIjKLMNOPQRSTUVWXYZ'
        word = w.upper().strip().replace(' ', '')

        return ''.join(x for x in word if x in alph)


    def _parse_word(self):

        with open('palavras.82eebac6.txt', 'r') as f:
            words = [x[:-1] for x in f.readlines()]

        res = []
        for word in words:
            if word[0] in self.w:
                if all(x in self.w and self.w.count(x) >= word.count(x) for x in word):
                    res.append(word)

        return [x for x in res if len(x) <= len(self.w)]


    def anagrams(self):

        l = self._parse_word()

        if bool('A' in self.w) ^ bool('I' in self.w):
            c = len(self.w) // 2 + 1
        elif 'I' in self.w and 'A' in self.w:
            c = len(self.w) // 2 + 2
        else:
            c = len(self.w) // 2

        for i in (combinations(l, x) for x in range(c)):
            for j in (x for x in i if len(''.join(x)) == len(self.w) and Counter(''.join(x)) == Counter(self.w)):
                print(' '.join(j))


# Programa Principal
s = input()
word = Anagram(s)
word.anagrams()