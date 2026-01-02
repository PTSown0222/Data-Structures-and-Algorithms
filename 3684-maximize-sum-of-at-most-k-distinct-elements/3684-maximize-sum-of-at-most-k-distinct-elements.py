class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums.sort(reverse = True)
        res = []

        for i in range(len(nums)):
            if nums[i] not in res and len(res) < k:
                res.append(nums[i])
        
        return res
