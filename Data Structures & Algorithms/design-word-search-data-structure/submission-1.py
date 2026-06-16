class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                cur.children[c] = TrieNode()
                cur = cur.children[c]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root
        def searchRecurse(word, cur):
            if not word and cur.end: return True
            if not word or  word[0]!='.' and word[0] not in cur.children: return False
            if word[0]=='.':
                return any([searchRecurse(word[1:], cur.children[c]) for c in cur.children])
            elif word[0] in cur.children: return searchRecurse(word[1:], cur.children[word[0]])
        return searchRecurse(word, cur)
