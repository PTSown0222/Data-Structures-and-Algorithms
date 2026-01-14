class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        
        n = len(sequence)
        m = len(word)

        dp = [0] * n

        for i in range(n):
            if i >= m - 1 and sequence[i - m + 1: i + 1] == word:
                if i - m >= 0:
                    dp[i] = dp[i - m] + 1
                else:
                    dp[i] = 1
        return max(dp) if dp else 0
