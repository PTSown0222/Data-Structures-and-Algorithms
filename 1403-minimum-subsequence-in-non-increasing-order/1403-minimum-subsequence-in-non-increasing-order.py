class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        
        res = []
        nums.sort(reverse = True)
        total = sum(nums)
        sum_v = 0
        for i in nums:
            sum_v += i
            res.append(i)

            remaining_sum = total - sum_v
            if sum_v > remaining_sum:
                return res
        return res