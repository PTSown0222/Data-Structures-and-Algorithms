class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        store = []
        if len(nums) == 0: return 0
        for i in range(len(nums)):
            if nums[i] != 0:
                # swap
                nums[k], nums[i] = nums[i], nums[k]
                k+=1