class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # process data
        # 1. positive or negative elements
        # 2. sorted or no unsorted
        # 3. unique or duplicate --> think of set()
        # 4. nums of elements --> nums[elements] if int : 1e6 (Cannot O(N^2)) -> try O(n)
        # or O(nlog(n))
        # 5. Space Complexity (I can use extra space or not)

        # [0, 0 ,1, 1,1,2,2]
        # l = 1 --> l - 1 = 0 and r += i
        # compare l - 1 and r
        if not nums: return 0
        curSum = 0
        left = 1
        n = len(nums)
        for right in range(1, n):
            if nums[right] != nums[left - 1]:
                nums[left] = nums[right]
                left += 1
        return left
