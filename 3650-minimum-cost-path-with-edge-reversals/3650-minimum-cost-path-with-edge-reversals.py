class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        
        # build adj_list
        G = defaultdict(list)

        for u, v, w in edges:
            G[u].append((v, w))
            G[v].append((u, 2 * w))
        
        min_heap = [(0,0)] # w = 0
        dist = {node : float('inf') for node in range(n)}
        #dist = [float('inf')] * n
        dist[0] = 0

        while min_heap:
            current_cost, u = heapq.heappop(min_heap)

            if u == n - 1:
                return current_cost
            
            if current_cost > dist[u]:
                continue
            
            if current_cost > dist[u]:
                continue
            
            # Duyệt hàng xóm
            for v, weight in G[u]:
                new_cost = current_cost + weight
                
                if new_cost < dist[v]:
                    dist[v] = new_cost
                    heapq.heappush(min_heap, (new_cost, v))
            
        return -1

        



