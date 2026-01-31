class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # S1: bruteforce
        # s = "cbaebabacd", p = "abc"
        # n = 10, m = 3
        # s[0:3]-->s[1:4]-->s[2:5]
        # def isAnagrams(a,b):
        #     return sorted(a) == sorted(b)
        # n = len(s)
        # m = len(p)
        # res = []
        # for i in range(n):
        #     # check anagrams of substrings s[i : i + m]
        #     if isAnagrams(s[i : i + m], p):
        #         res.append(i)
        # return res

        # S2: sliding window
        cnt = Counter(p)
        left = 0
        #print(cnt)
        res = []
        n = len(s)
        for right in range(n):
            char = s[right]
            cnt[char] -= 1
            while cnt[char] < 0:
                cnt[s[left]] += 1
                left += 1
            if right - left + 1 == len(p):
                res.append(left)
        return res


