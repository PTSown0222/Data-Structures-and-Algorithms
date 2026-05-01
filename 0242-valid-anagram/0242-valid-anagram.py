class Solution:
    
    def isAnagram(self, s: str, t: str) -> bool:
        def count_char(s):
            counts = {}
            for char in s:
                if char not in counts:
                    counts[char] = 0
                counts[char] += 1
            return counts
        
        return count_char(s) == count_char(t)
        