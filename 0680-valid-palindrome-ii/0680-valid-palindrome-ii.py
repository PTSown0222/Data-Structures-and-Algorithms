class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def is_palindrome(left, right):
            while left <= right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left = 0
        right = len(s) - 1

        while left <= right:
            #SELECT(P)
            char_left = s[left]
            char_right = s[right]

            # FEASIBLE(x)?
            if char_left == char_right:
                left += 1
                right -= 1
            else:
                del_left = is_palindrome(left + 1, right)
                del_right = is_palindrome(left, right - 1)

                return del_left or del_right
        return True

