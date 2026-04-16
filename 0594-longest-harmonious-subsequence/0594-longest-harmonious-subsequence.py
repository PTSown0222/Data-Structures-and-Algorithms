class Solution:
    def findLHS(self, nums: List[int]) -> int:
        
        nums.sort()
        n = len(nums)
        # (right - left) == 1
        left = 0
        max_len = 0
        for right in range(n):
            while nums[right] - nums[left] > 1:
                left += 1
            if nums[right] - nums[left] == 1:
                max_len = max(max_len, right - left + 1)
        return max_len