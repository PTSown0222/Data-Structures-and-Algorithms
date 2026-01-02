class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        # bắt cặp thì cứ nhỏ nhất - nhỏ nhất và lớn nhất-lớn nhất => trả về min thì vẫn là nhỏ + lớn vẫn tối ưu
        n = len(nums)
        minPairs = 0
        nums.sort()
        for i in range(0,n,2): # 0 , 2, 4 => nums[i] luôn là số nhỏ khi đã sort
            minPairs += nums[i]
        
        return minPairs 




