class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Connected Components

        n = len(isConnected)
        visited = [False] * n
        province = 0

        def dfs(i):
            visited[i] = True
            for j in range(n):
                if isConnected[i][j] == 1 and not visited[j]:
                    dfs(j)
        
        for i in range(n):
            if not visited[i]:
                province += 1
                dfs(i)
        
        return province