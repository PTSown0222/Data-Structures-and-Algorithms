class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if nums is None: return -1
        # get store is the first pointer to store val, if nums[i] != val
        # assign nums[store] = nums[i] to change the position, also is the position to return
        # 
        store = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[store] = nums[i]
                store +=1
        return store