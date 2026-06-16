class PrefixTree:

    def __init__(self):
        self.root = {'charMap': {}, 'end':False}

    def insert(self, word: str) -> None:
        if (len(word)==0): self.root['end']=True
        if len(word)>0:
            nextNode = PrefixTree() if word[0] not in self.root['charMap'] else self.root['charMap'][word[0]]
            self.root['charMap'][word[0]] = nextNode
            nextNode.insert(word[1:])

    def search(self, word: str) -> bool:
        if not word and self.root['end']:
            return True
        elif len(word)>0  and word[0] in self.root['charMap']:
            return self.root['charMap'][word[0]].search(word[1:])
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return True
        elif prefix and prefix[0] in self.root['charMap']:
            return self.root['charMap'][prefix[0]].startsWith(prefix[1:])
        else:
            return False