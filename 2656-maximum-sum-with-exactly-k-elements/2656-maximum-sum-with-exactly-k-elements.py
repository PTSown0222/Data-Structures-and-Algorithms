class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        
        nums.sort(reverse = True)

        max_sum = 0

        getMax = nums[0]

        for _ in range(k):
            max_sum += getMax
            getMax += 1
        
        return max_sum
