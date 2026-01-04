class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Đồ thị vô hướng, có trọng số
        
        # Cách 1 Giải thuật Floyd-Warshall áp dụng với n <= 100
        # dist = [[float('inf')] * n for _ in range(n)]
        # for i in range(n):
        #     dist[i][i] = 0
        
        # # build adj_matrix
        # for u, v, w in edges:
        #     dist[u][v] = w
        #     dist[v][u] = w 
        
        # for k in range(n):
        #     for i in range(n):
        #         for j in range(n):
        #             if dist[i][k] + dist[k][j] < dist[i][j]:
        #                 dist[i][j] = dist[i][k] + dist[k][j]
        
        # min_neighbors = float('inf') # 1e9
        # result_city = -1

        # for i in range(n):
        #     count = 0
        #     for j in range(n):
        #         if i != j and dist[i][j] <= distanceThreshold:
        #             count += 1
            
        #     if count <= min_neighbors:
        #         min_neighbors = count
        #         result_city = i
        
        # return result_city

        # Cach 2 Dijkstra
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        def get_reachable_count(start_node):
            min_heap = [(0, start_node)]
            distances = {node: float('inf') for node in range(n)}
            distances[start_node] = 0
            
            reachable_count = 0
            
            while min_heap:
                current_dist, u = heapq.heappop(min_heap)
                
                # Nếu khoảng cách đã vượt quá ngưỡng thì không cần xét tiếp
                # các đường đi dài hơn từ đỉnh này nữa.
                if current_dist > distanceThreshold:
                    continue

                if current_dist > distances[u]:
                    continue

                # Duyệt các hàng xóm v của u
                for v, weight in graph[u]:
                    new_dist = current_dist + weight
                    # Nếu tìm thấy đường ngắn hơn
                    if new_dist < distances[v]:
                        distances[v] = new_dist
                        heapq.heappush(min_heap, (new_dist, v))
            
            for node in range(n):
                if node != start_node and distances[node] <= distanceThreshold:
                    reachable_count += 1
            return reachable_count

        min_neighbors = float('inf')
        result_city = -1
        
        for i in range(n):
            count = get_reachable_count(i)
            if count <= min_neighbors:
                min_neighbors = count
                result_city = i
                
        return result_city