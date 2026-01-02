class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        
        n = len(colors)
        distance1 = 0

        for i in range(n - 1, 0, -1):
            if colors[0] != colors[i]:
                distance1 = i - 0
                break
        
        distance2 = 0
        for i in range(n):
            if colors[i] != colors[n - 1]:
                distance2 = n - 1 - i
                break
        
        return max(distance1 , distance2)
