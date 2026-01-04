class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # directed graph and weights => use Dijkstra Algo
        # graph[u] = [(v1, time1), (v2, time2)...]
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        # (accumulate time, Current_Node)
        # Nếu là A* thì cứ ước lượng khoảng cách min_heap = [(4,k)]
        min_heap = [(0, k)]
        
        # dictionary lưu thời gian ngắn nhất đến từng node = infinity
        # dist = {"A" : "infinity"}
        dist = {node: float('inf') for node in range(1, n + 1)}
        dist[k] = 0

        while min_heap:
            current_time, u = heapq.heappop(min_heap) # 0, k
            # tìm thời gian tốt nhất, nếu thời gian mình pop ra mà lớn hơn thời gian trong dist thì bỏ qua, còn nếu mà nhỏ hơn thì pop cái đỉnh thời gian ngắn nhất ra
            if current_time > dist[u]:
                continue
            
            for v, travel_time in graph[u]:
                new_time = current_time + travel_time

                if new_time < dist[v]:
                    dist[v] = new_time
                    
                    heapq.heappush(min_heap, (new_time, v))
        
        max_wait = max(dist.values())
        # Nếu vẫn còn node giá trị là Vô cực -> Không liên thông -> Trả về -1
        return max_wait if max_wait < float('inf') else -1
