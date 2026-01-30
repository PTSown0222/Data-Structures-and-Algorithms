class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # S1: bruteforce
        n = len(s)
        ans = float("-inf")
        for i in range(n):
            seen = set()
            for j in range(i,n):
                if s[j] in seen:
                    break
                else:
                    ans = max(ans, j - i + 1)
                    seen.add(s[j])
        return ans if ans != float("-inf") else 0