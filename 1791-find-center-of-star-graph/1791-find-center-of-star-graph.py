# class Solution:
#     def findCenter(self, edges: List[List[int]]) -> int:
        
#         edge1 = edges[0]
#         edge2 = edges[1]

#         if edge1[0] == edge2[0] or edge1[0] == edge2[1]:
#             return edge1[0]
#         else:
#             return edge1[1]


#--- adj_list---#
from collections import defaultdict

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        total_edges = len(edges) 
        for node in graph:
            if len(graph[node]) == total_edges:
                return node
                
        return -1