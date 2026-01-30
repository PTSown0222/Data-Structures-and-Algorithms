class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # S1: bruteforce
        n = len(s)
        # ans = float("-inf")
        # for i in range(n):
        #     seen = set()
        #     for j in range(i,n):
        #         if s[j] in seen:
        #             break
        #         else:
        #             ans = max(ans, j - i + 1)
        #             seen.add(s[j])
        # return ans if ans != float("-inf") else 0

        # S2: sliding_window

        left = 0
        seen = set()
        res = float("-inf")
        for right in range(n):
            char = s[right]
            while char in seen:
                if s[left] in seen:
                    seen.remove(s[left])
                left += 1
            seen.add(char)
            res = max(res,right - left + 1)
        return res if res != float("-inf") else 0
            

