class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # tương tự như bài toán jump frog -> dùng tham lam
        max_goal = 0
        res = 0
        last_index = len(nums) - 1

        for i in range(len(nums)):
            # kiểm tra trường hợp vị trí hiện tại > điểm cuối hay không
            if i > max_goal:
                return False
            
            max_goal = max(max_goal ,i + nums[i])
            if max_goal >= last_index:
                return True
        return False 
            