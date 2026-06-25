class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False]*(n+1)
        dp[-1] = True
        for i in range(n-1, -1, -1):
            for word in wordDict:
                if dp[i]: break
                if (n-i)>=len(word):
                    w = len(word)
                    if s[i: i+w]==word:
                        print(word)
                        dp[i] = dp[i+w]
        print(dp)
        return True if dp[0] else False