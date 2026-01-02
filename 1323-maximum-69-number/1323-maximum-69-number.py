class Solution:
    def maximum69Number (self, num: int) -> int:
        
        digits = list(str(num)) # convert to list
        n = len(digits)
        for i in range(n):
            if digits[i] == "6":
                digits[i] = "9"
                break
        
        return int("".join(digits))