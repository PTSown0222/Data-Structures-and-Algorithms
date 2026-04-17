class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        arr = list(s)
        steps = 2*k
        for i in range(0,n,steps):
            arr[i:i+k] = reversed(arr[i:i+k])
        return "".join(arr)