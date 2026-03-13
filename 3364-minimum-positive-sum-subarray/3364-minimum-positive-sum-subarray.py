class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        
        # the smallest positive curSum
        # length of window >= l and <= r 
        n = len(nums)
        left = 0
        ans = float("inf")

        for right in range(n):
            curSum = 0
            for left in range(right, -1, -1):
                curSum += nums[left]
                length = right - left + 1
            
                if length > r:
                    break
                
                if length >= l:
                    if curSum > 0:
                        ans = min(ans, curSum)
        
        return -1 if ans == float("inf") else ans