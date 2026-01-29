class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # BRUTE FORCE
        #O(N^3)
        #s = "babad" -> aba
        # def isPalindrome(s,l,r):
        #     while l < r:
        #         if s[l] != s[r]:
        #             return False
        #         l+=1
        #         r-=1
        #     return True

        # check the first chac and the last chac if use topdown DP
        # O(N^2) - hashmap = dict
        # @lru_cache(None)
        # def isPalindrome(s,l,r):
        #     if l >= r:
        #         return True
        #     return s[l] == s[r] and isPalindrome(s,l+1,r-1)

        # use memo = []
        memo = [ [None] * n for _ in range(n)] # a table stored value
        def isPalindrome(s, l ,r):
            if l >= r: return True
            if memo[l][r] != None: return memo[l][r]
            if s[l] != s[r]: return False
            memo[l][r] = isPalindrome(s,l+1,r-1)
            return memo[l][r]


        
        resLen = 0
        resStartIndex = 0
        for i in range(n):
            for j in range(i, n):
                if isPalindrome(s, i, j) and j - i + 1 > resLen:
                    resLen = j - i + 1
                    resStartIndex = i
        
        return s[resStartIndex : resStartIndex + resLen]

        # s = "babad"
        # i = 0 --> n => 0
        # j = i --> n => 0 => resLen = 0 - 0 + 1 = 1
        # j = 1, ba-notPalin,
        # j = 2, bab => j - i + 1= 2 - 0 + 1 = 3 update resLen = 3, index = i = 0
        # s[0 : 0 + 3] = s[0:3] : 3 char - bab

