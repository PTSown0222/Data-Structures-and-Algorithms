class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        # i + j + k + m = target
        # i + j = tar - k - m
        res = set()
        n = len(nums)
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                left = j + 1
                right = n - 1
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if current_sum == target:
                        res.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1
                    elif current_sum < target:
                        left += 1
                    else:
                        right -= 1
                    
        return [list(t) for t in res]
