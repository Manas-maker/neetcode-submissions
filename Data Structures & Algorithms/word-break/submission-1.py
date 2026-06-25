class Trie:
    def __init__(self):
        self.children = {}
        self.end = False
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trieRoot = Trie()
        n = len(s)
        def searchWord(rootNode, s, i , j):
            cur = rootNode
            for index in range(i, j+1):
                if s[index] not in cur.children: return False
                cur = cur.children[s[index]]
            return cur.end
        for i in wordDict:
            cur = trieRoot
            for c in i:
                if c in cur.children:
                    cur = cur.children[c]
                else:
                    cur.children[c] = Trie()
                    cur = cur.children[c]
            cur.end = True
        dp = [False]*(n+1)
        dp[n] = True
        t = 0
        for i in wordDict:
            t = max(t, len(i))
        for i in range(n, -1, -1):
            for j in range(i, min(n, i+t)):
                if searchWord(trieRoot, s, i, j):
                    dp[i] = dp[j+1]
                    if dp[i]: break
        print(dp)
        return dp[0]
