class Solution:
    def reverseVowels(self, s: str) -> str:
        vow = ["a","A","e","E", "i", "I", "o","O", "u", "U"]
        n = len(s)
        s = list(s)
        left = 0
        right = n - 1
        while left < right:
            if s[left] in vow and s[right] in vow:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif s[left] not in vow:
                left += 1
            elif s[right] not in vow:
                right -= 1
        return "".join(s)
            