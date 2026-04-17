class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        if n == 1:
            return nums[0]
        left = 0
        curr_sum = 0
        ans = float('-inf')
        for right in range(n):
            curr_sum += nums[right]

            if right - left + 1 > k:
                curr_sum -= nums[left]
                left += 1

            if right - left + 1 == k:
                ans = max(ans, curr_sum)
        return ans/k