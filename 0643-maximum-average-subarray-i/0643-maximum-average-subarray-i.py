class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        # dynamic sliding window
        # left = 0
        # curr_sum = 0
        # ans = float('-inf')
        # for right in range(n):
        #     curr_sum += nums[right]

        #     if right - left + 1 > k:
        #         curr_sum -= nums[left]
        #         left += 1

        #     if right - left + 1 == k:
        #         ans = max(ans, curr_sum)
        # return ans/k

        # fixed sliding window

        current_window_sum = sum(nums[:k])
        max_sum = current_window_sum

        for i in range(k, n):
            current_window_sum = current_window_sum + nums[i] - nums[i - k]
  
            if current_window_sum > max_sum:
                max_sum = current_window_sum
        return max_sum/k
