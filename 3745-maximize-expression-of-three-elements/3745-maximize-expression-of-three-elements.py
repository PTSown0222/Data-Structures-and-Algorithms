class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        
        nums.sort()
        n = len(nums)

        a = nums[n - 1]
        b = nums[n - 2]
        c = nums[0]

        return a+b-c
