class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s) # 4
        low = 0
        high = n
        res = []

        for i in range(n):
            if s[i] == "I":
                res.append(low)
                low += 1
            elif s[i] == "D":
                res.append(high)
                high -= 1
        res.append(low)
        return res
                

