class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        if n < 3:
            return 0
        
        left = 0
        for right in range(2,n):
            # check arithmetic
            if nums[right] - nums[right - 1] == nums[right - 1] - nums[right - 2]:
                ans += (right - left + 1) - 2
            else:
                left = right - 1
        return ans

        
        