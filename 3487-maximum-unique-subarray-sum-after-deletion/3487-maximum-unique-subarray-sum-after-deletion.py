class Solution:
    def maxSum(self, nums: List[int]) -> int:
        total = 0
        se = set()
        max_val = max(nums)
        if max_val < 0:
            return max_val
        for i in range(len(nums)):
            if nums[i] > 0:
                se.add(nums[i])
        for j in se:
            total += j
        return total
