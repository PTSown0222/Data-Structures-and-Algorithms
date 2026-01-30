class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # solution 1: bruteforce O(N ^ 2)
        n = len(numbers)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if numbers[i] + numbers[j] == target:
        #             return [i + 1, j + 1]

        # solution 2: hashtable
        # seen = {}
        # numbers = [2,7,11,15], target = 9
        # i = 0 , 1, 2, 3
        # b = 2, a = 7, if 7 in seen => (seen[7] + 1, 0 + 1)
        # seen[2] = i = 0
        # b = 7, a = 2, if 2 in seen => (seen[2]==0 + 1, 1 + 1)
        # seen = {}
        # for ind, b in enumerate(numbers):
        #     a = target - b
        #     if a in seen:
        #         return [seen[a] + 1, ind+1]
        #     seen[b] = ind

        # solution 3: binary search

        def binarySeach(numbers, l, r, target):
            while l <= r:
                mid = (l + r) // 2
                if numbers[mid] == target:
                    return mid
                if numbers[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1
        
        for i in range(n):
            res = binarySeach(numbers, i + 1, n - 1, target - numbers[i])
            if res != -1:
                return [i + 1, res + 1]

        
                

        
