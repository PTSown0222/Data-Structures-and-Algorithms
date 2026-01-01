class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # cho inputs -> unique
        # output: must not duplicate subsets
        res = []
        curr_path = []
        n = len(nums)
        
        def TRY(i):
            # Vì tập con độ dài bao nhiêu cũng lấy (kể cả rỗng)
            # Không cần đợi if i == n mới append
            res.append(curr_path[:])
            for j in range(i, n):
                curr_path.append(nums[j])
                TRY(j + 1)
                curr_path.pop()
        TRY(0)
        return res