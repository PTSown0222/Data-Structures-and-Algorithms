class Solution:
    def reverseWords(self, s: str) -> str:
        # n = len(s)
        # arr = list(s)
        # left = 0
        # pos = 0
        # for right in range(n + 1):
        #     if right == n or arr[right] == " ":
        #         start, end = left, right - 1
        #         while start < end:
        #             arr[start], arr[end] = arr[end], arr[start]
        #             start += 1
        #             end -= 1
                
        #         left = right + 1
        # return "".join(arr)

        # more pythonic
        return " ".join([w[::-1] for w in s.split(" ")])


                
