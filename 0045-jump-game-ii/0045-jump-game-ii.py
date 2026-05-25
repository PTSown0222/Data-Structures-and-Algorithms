class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        max_goal = 0
        step = 0
        current = 0

        for i in range(n - 1):
            max_goal = max(max_goal, i + nums[i])
            if i == current:
                step+=1
                current = max_goal

        return step
