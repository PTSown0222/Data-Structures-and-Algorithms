class Solution:
    def climbStairs(self, n: int) -> int:
        
        # find a optimal subproblem
        # find a recursive formulate => dp[i] = dp[i - 1] + dp[i - 2]
        # basecase one steps => n = 1, 2 steps = 1 + 1
        # init dp array with n elements
        dp = [0] * (n+1)

        if n <= 2:
            return n
        
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
        


