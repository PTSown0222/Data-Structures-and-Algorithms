class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # left = 0
        # window = right - left + 1
        n = len(s)
        prev = 0
        left = 0
        ans = 0
        for right in range(1,n + 1):
            if right == n or s[right] != s[right - 1]:
                curr_group_len = right - left
                ans += min(prev, curr_group_len)
                prev = curr_group_len
                left = right
        return ans