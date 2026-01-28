class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # top-down DP
        n = len(s)
        wordSet = set(wordDict)
        # @lru_cache(None)
        # def dp(i):
        #     if i == n:
        #         return True
        #     for j in range(i, n):
        #         word = s[i : j + 1]
        #         if word in wordSet and dp(j + 1):
        #             return True
        #     return False
        # return dp(0)

        # bottom-up DP

        dp = [False] * (n + 1)

        # basecase --> empty string 
        dp[0] = True

        for i in range(1, n+ 1):
            for j in range(i):
                if dp[j] == True and s[j : i] in wordSet:
                    dp[i] = True
                    break
        return dp[n]