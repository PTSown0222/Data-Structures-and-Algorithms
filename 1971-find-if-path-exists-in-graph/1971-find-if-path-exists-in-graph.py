class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # code by BFS
        visited = [False] * n 
        visited[source] = True
        
        # build Adj List
        adj = [[] for _ in range(n)]

        # traverse
        for i in range(len(edges)):
            u = edges[i][0]
            v = edges[i][1]
            
            adj[u].append(v) 
            adj[v].append(u) 

        queue = [source]
        while len(queue) > 0:
            current_node = queue.pop(0)
            
            if current_node == destination:
                return True
            
            for neighbor in adj[current_node]:
                if visited[neighbor] == False:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return False

        # time complexity O(V + E) with the number of vertices and E being the number of edges
        # space complexity O(V + e)

