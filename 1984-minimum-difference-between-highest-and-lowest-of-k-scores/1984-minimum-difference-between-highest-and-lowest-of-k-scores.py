class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1: return 0
        nums.sort()
        n = len(nums)
        res = float('inf')
        left = 0
        n_windows_K = n - k + 1
        #length_window = right - left + 1
        #right = left + k - 1
        for right in range(n_windows_K):
            current_diff = nums[right + k - 1] - nums[right]
            res = min(res, current_diff)
        return res
            

