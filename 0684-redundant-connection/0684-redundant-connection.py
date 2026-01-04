class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #DSU (Disjoint Set Union) - Union-Find
        # count edges - đếm cạnh
        n = len(edges)
        parent = list(range(n + 1))

        def find(node):
            if parent[node] == node:
                return node
            parent[node] = find(parent[node]) 
            return parent[node]
        
        def union(u, v):
            root_u = find(u)
            root_v = find(v)

            # 2 root thông với nhau => có chu trình
            if root_u == root_v:
                return False
            
            parent[root_u] = root_v
            return True
        for u, v in edges:
            if union(u, v) == False:
                return [u, v]
        
        return []
