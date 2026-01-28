class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp(amount) = Return the fewest number of coins 

        @lru_cache(None)
        def dp(amount):
            if amount < 0:
                return float("inf")
            #no amount == no coin
            if amount == 0:
                return 0
            ans = float("inf")
            for coin in coins:
                ans = min(ans, dp(amount - coin) + 1)
            
            return ans
        res = dp(amount)
        return -1 if res == float("inf") else res
