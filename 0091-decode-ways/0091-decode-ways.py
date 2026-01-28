class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # 226 : 3ways (2 2 6) = (BBF), (2 26) = (B Z), (22 6) = (V F)
        # dp(i) is the number of ways to decode s[i --> n-1]
        # dp(0) --> results
        # top-down DP
        @lru_cache(None)
        def dp(i):
            if i == n: return 1 # empty string = 1 way
            # case 1: only 1 digit : 1...9
            ans = 0
            if s[i] != "0":
                ans += dp(i + 1)
            # case 2: 10 --> 26
            if i + 1 < n and (s[i] == "1" or s[i] == "2" and s[i + 1] <= "6"):
                ans += dp(i + 2)
            return ans
        return dp(0)
