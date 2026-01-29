class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # dp[i] = length of increasing subsequeces from nums[0...i] include nums[i] as a last element
        # nums = [10,9,2,5,3,7,101,18]
        # dp[0] = 1
        # dp[1] = 1
        # dp[2] = 1
        # dp[3] = 2, [2,5]
        # dp[i] = max(dp[j] with j < i) and (nums[j] < nums[i]) + nums[i]
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)