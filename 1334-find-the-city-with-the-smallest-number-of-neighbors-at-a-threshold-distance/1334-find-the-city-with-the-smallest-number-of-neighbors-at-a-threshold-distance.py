class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Đồ thị vô hướng, có trọng số
        
        # Cách 1 Giải thuật Floyd-Warshall áp dụng với n <= 100
        dist = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        
        # build adj_matrix
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w 
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        min_neighbors = float('inf') # 1e9
        result_city = -1

        for i in range(n):
            count = 0
            for j in range(n):
                if i != j and dist[i][j] <= distanceThreshold:
                    count += 1
            
            if count <= min_neighbors:
                min_neighbors = count
                result_city = i
        
        return result_city