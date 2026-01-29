class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp(i) is the maximum amount of money in house [0..i]
        # case 1 if dp[i] = nums[i] + dp[i- 2]
        # case 2 if not dp[i] => dp[i -1]
        n = len(nums)
        if n == 1: return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            take = nums[i] + dp[i- 2]
            skip = dp[i-1]
            dp[i] = max(take,skip)
        return dp[n-1]


