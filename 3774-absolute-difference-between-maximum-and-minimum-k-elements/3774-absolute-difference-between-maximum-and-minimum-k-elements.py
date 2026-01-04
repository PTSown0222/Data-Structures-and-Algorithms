class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        if len(nums) == 1:
            return 0

        return abs(sum(nums[-k:]) - sum(nums[:k]))