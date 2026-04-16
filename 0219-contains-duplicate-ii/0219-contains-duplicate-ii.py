class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #bruteforce : TLE
        n = len(nums)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if nums[i] == nums[j] and abs(i - j) <= k:
        #             return True
        # return False

        # sliding window
        window = set()
        left = 0
        for right in range(n):

            if right - left > k:
                window.remove(nums[left])
                left+=1
            
            if nums[right] in window:
                return True
            window.add(nums[right])
        
        return False

            

