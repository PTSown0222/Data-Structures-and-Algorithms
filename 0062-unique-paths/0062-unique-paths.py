class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        #init a 2D DP
        dp = [[0] * n for _ in range(m)]

        for row in range(m):
            for col in range(n):
                if row == 0 and col == 0:
                    dp[row][col] = 1
                else:
                    dp[row][col] = dp[row-1][col] + dp[row][col-1]
        
        return dp[m-1][n-1]
        