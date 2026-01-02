class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort(key = lambda x:-x)
        for i in range(len(nums) - 2):
            a = nums[i] # maximum 
            b = nums[i + 1]
            c = nums[i + 2]

            if c + b > a:
                return a + b + c  
        return 0