# class Solution:
#     def minimumDifference(self, nums: List[int], k: int) -> int:
#         if k == 1: return 0
#         nums.sort()
#         n = len(nums)
#         res = float('inf')
#         # hard window - Khi đề bài cho chỉ số window kết thúc là K
#         n_windows_K = n - k + 1
#         for i in range(n_windows_K):
#             first_k = i
#             last_k = i + k - 1
#             window = nums[last] - nums[first]
#             res = min(res, window)
#         return res
            
# dynamic window - khi chưa biết đề bài cho chỉ số window cuối là bao nhiêu chỉ cho target duy nhất
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1: return 0
        nums.sort()
        n = len(nums)
        res = float('inf')
        left = 0
        for right in range(n):
            if right - left + 1 == k:
                res = min(res, nums[right] - nums[left])
                left += 1
        return res

        