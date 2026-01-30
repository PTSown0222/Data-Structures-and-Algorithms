class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        # S1 : bruteforce 

        # S2: 2-pointers
        #nums[i] + nums[j] + nums[k] == 0
        # => nums[i] + nums[j] == -nums[k]
        # k = 0, j = 1 --> n - 1
        # int, str --> hastable
        # object -> imple hashcode, equals
        res = set() # min1, min2, min3
        nums.sort()
        for k in range(n):
            # two sums in range [k + 1 : n - 1]
            target = -nums[k]
            l = k + 1
            r = n - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    res.add((nums[k], nums[l], nums[r]))
                    l+=1
                    r-=1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return [list(triplet) for triplet in res]

