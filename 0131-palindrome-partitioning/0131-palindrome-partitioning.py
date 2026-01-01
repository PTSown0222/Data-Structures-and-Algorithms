class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        curr_path = []
        res = []
        n = len(s)
        # Hàm kiểm tra chuỗi đối xứng (Palindrome)
        def is_palindrome(s):
            return s == s[::-1]
        
        def TRY(i):

            for j in range(i, n):
                
                substr = s[i : j + 1] # [0: 0 + 1] => [0 : 1] = "aa" => check palin

                if is_palindrome(substr):
                    curr_path.append(substr)
                
                    if j < n - 1:
                        TRY(j + 1)
                    else:
                        res.append(curr_path[:])
                    
                    curr_path.pop()
        TRY(0)
        return res
