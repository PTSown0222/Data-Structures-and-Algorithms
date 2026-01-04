class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        d = {}

        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
        
        for i in d.values():
            if i > 1:
                return True
        return False