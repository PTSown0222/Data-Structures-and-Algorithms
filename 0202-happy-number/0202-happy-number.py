class Solution:
    def isHappy(self, n: int) -> bool:
        se = set()
        # 23 = 3 ** 2 + 2 **2 = 9 + 4 = 13 = 9**2 + 4**2=81+16
        def _sum_square(n):
            output = 0
            while n:
                digit = n % 10
                output += digit ** 2
                n = n // 10
            return output
        while n not in se:
            se.add(n)
            n = _sum_square(n)
            if n == 1:
                return True
        return False