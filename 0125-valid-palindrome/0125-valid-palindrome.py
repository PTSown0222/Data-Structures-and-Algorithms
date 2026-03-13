class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # palindrome is acca, ACca
        # s.empty() --> True
        if len(s) == 0:
            return True
        
        ispalindromestr = ""
        for char in s:
            if char.isalpha() or char.isdigit():
                ispalindromestr += char.lower()
        return ispalindromestr == ispalindromestr[::-1]
    
        
        
