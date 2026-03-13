class Solution:
    def myAtoi(self, s: str) -> int:
        
        # 1 whitespace
        s = s.strip()

        if len(s) == 0:
            return 0

        # 2. signedness
        sign = 1
        if (s[0] == "-") or (s[0] == "+"):
            if s[0] == "-":
                sign = -1
            s = s[1:]

        # 3. Conversion
        digit_s = ""
        for c in s:
            if c.isdigit():
                digit_s += c
            else:
                break
        
        if len(digit_s) > 0:
            ans = int(digit_s) * sign
        else:
            ans = 0

        # 4. Rounding
        if ans < -2**31:
            ans = -2**31
        elif ans > 2**31 - 1:
            ans = 2**31 - 1
    
        return ans