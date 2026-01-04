class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # we have [1,2,3,4], target = 9
        # subtract 9 -1 = 8, find 8 in this array. If having 8 return 1 and 8
        # d = {0 : 2, 1 : 7, 2 : 11, 3 : 15}
        # getting value we only need O(1) to access
        d = {}

        for ind, val in enumerate(nums):
            
            diff = target - val

            if diff in d:
                return [d[diff],ind]
            
            d[val] = ind
        return []
        

