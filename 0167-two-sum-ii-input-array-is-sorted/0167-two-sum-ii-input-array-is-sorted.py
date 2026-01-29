class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # solution 1: bruteforce O(N ^ 2)
        n = len(numbers)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if numbers[i] + numbers[j] == target:
        #             return [i + 1, j + 1]

        # solution 2: hashtable
        seen = {}
        for ind, b in enumerate(numbers):
            a = target - b
            if a in seen:
                return [seen[a] + 1, ind+1]
            seen[b] = ind