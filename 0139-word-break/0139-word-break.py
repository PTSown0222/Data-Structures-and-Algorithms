class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordSet = set(wordDict)

        @lru_cache(None)
        def dp(i):
            if i == n:
                return True
            for j in range(i, n):
                word = s[i : j + 1]
                if word in wordSet and dp(j + 1):
                    return True
            return False
        return dp(0)