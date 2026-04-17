class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        
        ans = []
        n = len(nums)
        pos = 0

        for j in range(n):
            if nums[j] == key:
                start = max(pos, j - k)
                end = min(n-1,j+k)
            
                for i in range(start, end+1):
                    ans.append(i)
                pos = end + 1
        return ans