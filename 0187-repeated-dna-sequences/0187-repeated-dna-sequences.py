class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # hash set + sliding window
        n = len(s)
        k = 10
        seen = set()
        repeated = set()
        for i in range(n - k + 1):
            sub_adn_seq = s[i:i+k]
            if sub_adn_seq in seen:
                repeated.add(sub_adn_seq)
            else:
                seen.add(sub_adn_seq)
        return [i for i in repeated]
        
        # hashmap + sliding window : TLE
        # n = len(s)
        # k = 10
        # ans = []
        # freq = {}
        # for i in range(n - k + 1):
        #     window = s[i : i + k]
        #     freq[window] = freq.get(window,0) + 1
        #     print(freq)
        
        #     if freq[window] == 2:
        #         ans.append(window)
        
        # return ans