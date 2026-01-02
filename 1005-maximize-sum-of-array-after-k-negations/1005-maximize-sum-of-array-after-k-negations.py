class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        cnt = 0
        for i in range(len(nums)):
            if k > 0 and nums[i] < 0:
                nums[i] = -nums[i]
                k -= 1
        
        if k > 0:
            if k % 2 != 0:
                nums.sort()
                nums[0] = -nums[0]
            
        for i in range(len(nums)):
            cnt += nums[i]
        return cnt

