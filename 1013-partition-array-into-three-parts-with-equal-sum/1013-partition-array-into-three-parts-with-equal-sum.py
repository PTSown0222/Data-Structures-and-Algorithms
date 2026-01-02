class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        # sum % 3 == 0
        total = 0
        for i in range(len(arr)):
            total += arr[i]
        if total % 3 != 0:
            return False
        
        target = total / 3

        cnt = 0
        part = 0
        for j in range(len(arr)):
            cnt += arr[j]
            if cnt == target:
                part += 1
                cnt = 0
        return part >= 3

        
