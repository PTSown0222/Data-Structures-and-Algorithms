class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        
        n = len(nums)
        # init the dictionary in python
        counts = {}

        # count the frequency
        for i in range(n):
            val = nums[i]

            if val in counts:
                counts[val] += 1
            else:
                counts[val] = 1

            if counts[val] > 1:
                return val
