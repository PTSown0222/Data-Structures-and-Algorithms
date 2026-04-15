class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1: return 0
        nums.sort()
        n = len(nums)
        res = float('inf')
        # hard window - Khi đề bài cho chỉ số window kết thúc là K
        n_windows_K = n - k + 1
        for i in range(n_windows_K):
            first = i
            last = i + k - 1
            window = nums[last] - nums[first]
            res = min(res, window)
        return res
            
# dynamic window - khi chưa biết đề bài cho chỉ số window cuối là bao nhiêu chỉ cho target duy nhất
# class Solution:
#     def minimumDifference(self, nums: List[int], k: int) -> int:
#         if k == 1: return 0
#         nums.sort()
#         n = len(nums)
#         res = float('inf')
#         # hard window
#         left = 0

        