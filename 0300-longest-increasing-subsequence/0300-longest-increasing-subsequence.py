class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        t = [-1] * n
        iMax = 0
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    t[i] = j
            if dp[i] > dp[iMax]:
                iMax = i
        
        path = []
        i = iMax
        while i != -1:
            path.append(i)
            i = t[i]
        
        print(f"path:")
        for i in range(len(path) - 1,-1,-1):
            print(nums[path[i]])
        return dp[iMax]
        