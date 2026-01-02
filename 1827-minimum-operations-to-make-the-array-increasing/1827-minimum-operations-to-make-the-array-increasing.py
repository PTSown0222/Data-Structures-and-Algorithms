class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt =0
        # len(nums) = 5
        for i in range(len(nums) - 1):
            # nums[i + 1] = 2 <= 5, 
            if nums[i + 1] <= nums[i]:
                cnt += nums[i] + 1 - nums[i + 1]
                nums[i + 1] = nums[i] + 1
        return cnt
        
