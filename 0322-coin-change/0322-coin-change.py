class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp(amount) = Return the fewest number of coins 

        # top-down DP
        # @lru_cache(None)
        # def dp(amount):
        #     if amount < 0:
        #         return float("inf")
        #     #no amount == no coin
        #     if amount == 0:
        #         return 0
        #     ans = float("inf")
        #     for coin in coins:
        #         ans = min(ans, dp(amount - coin) + 1)
            
        #     return ans
        # res = dp(amount)
        # return -1 if res == float("inf") else res

        # Bottom-up
        dp = [float('inf')] * (amount + 1)
        
        dp[0]=0
        for i in range(amount +1):
            for coin in coins:
                if i  >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1


