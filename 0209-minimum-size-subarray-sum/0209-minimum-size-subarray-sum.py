class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # S1: brute force
        n = len(nums)
        # res = float("inf")
        # for i in range(n):
        #     curSum = 0 # sum of subarray from nums[i --> j]
        #     for j in range(i,n):
        #         curSum += nums[j]
        #         if curSum >= target:
        #             res = min(res, j - i + 1)
        #             break
        # return res if res != float("inf") else 0
        
        # S2: Dynamic window
        left = 0
        curSum = 0
        res = float("inf")
        for right in range(n): # giãn cửa sổ ra
            # Cộng dồn right là chỉ số  kết thúc của cửa sổ
            curSum += nums[right]
            while curSum >= target:
                res = min(res, right - left + 1)
                # right - left + 1 = dynamic window : đây là cửa sổ co dã
                curSum -= nums[left]
                left += 1 # co cửa sổ lại
        return res if res != float("inf") else 0

