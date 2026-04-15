class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        print(nums)

        ans = 0
        n = len(nums)
        ans = nums[0] + nums[1] + nums[2]
        
        for k in range(n):
            sums = 0
            left = k + 1
            right = n - 1
            while left < right:
                current_sum = nums[k] + nums[left] + nums[right]
                if current_sum == target:
                    return current_sum
                
                if abs(current_sum - target) < abs(ans - target):
                    ans = current_sum
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
        return ans
