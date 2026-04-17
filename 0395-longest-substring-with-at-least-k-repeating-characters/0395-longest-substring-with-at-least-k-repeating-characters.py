class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # s = "ababbc", k = 2, len = 6
        # Formula: Một cửa sổ bắt đầu tại index thứ i, cần cửa sổ cỡ k, nằm trọn
        # trong mảng có kích thước là n thì vị trí kết thúc là i + k - 1 < n - 1
        # => i < n - k Vậy from i --> n - k + 1 là sẽ không lo tràn số
        # Vậy cửa sổ cố định là arr[i : i + k] --> với cửa sổ cố định
        n = len(s)
        max_len = 0

        for i in range(0,27):
            freq = {}
            left = 0
            unique_cnt = 0
            at_least_k = 0

            for right in range(n):
                char_r = s[right]
                freq[char_r] = freq.get(char_r, 0) + 1
                if freq[char_r] == 1:
                    unique_cnt += 1
                if freq[char_r] == k:
                    at_least_k += 1
                
                while unique_cnt > i:
                    char_l = s[left]
                    if freq[char_l] == k:
                        at_least_k -= 1
                    freq[char_l] -= 1
                    if freq[char_l] == 0: 
                        unique_cnt -= 1
                    left += 1
                if unique_cnt == i and unique_cnt == at_least_k:
                    max_len = max(max_len, right - left + 1)

        return max_len

        
                
                

                
