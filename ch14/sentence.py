import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)
    
    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self) -> str:
        return 'Sentence(%s)' % reprlib.repr(self.text)

s = Sentence('"The time has come," the Walrus said,')
print(s)
for word in s:
    print(word)

print( list(s) ) 
print( s[0], s[-1], s[5])