# class Solution:
#     def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
#         # code by BFS - clear
#         visited = [False] * n 
#         visited[source] = True
        
#         # build from edege-List to Adj-List
#         adj = [[] for _ in range(n)]
#         for i in range(len(edges)):
#             u = edges[i][0]
#             v = edges[i][1]
            
#             adj[u].append(v) 
#             adj[v].append(u) 

#         queue = [source]
#         while len(queue) > 0:
#             current_node = queue.pop(0)
            
#             if current_node == destination:
#                 return True
            
#             for neighbor in adj[current_node]:
#                 if visited[neighbor] == False:
#                     visited[neighbor] = True
#                     queue.append(neighbor)
#         return False

        # time complexity O(V + E) with the number of vertices and E being the number of edges
        # space complexity O(V + e)

#------DFS-----#

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #graph = {0: []}
        graph = collections.defaultdict(list)
        for u, v in edges:
            #graph = {0: [1]}
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node:int, visted: List[int]):
            
            if node == destination:
                return True
            
            # visited -> it's used
            visited.add(node)

            #graph = {0: [1, 2, 3]}
            # for neighbor in [1,2,3]:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor, visited):
                        return True
            return False
        
        visited = set()
        return dfs(source, visited)


            

