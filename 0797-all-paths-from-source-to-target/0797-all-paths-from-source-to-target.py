class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # DFS + Backtracking
        target = len(graph) - 1
        result = []

        def dfs(node, path):
            if node == target:
                result.append(path[:])
                return

            for neighbor in graph[node]:
                path.append(neighbor)
                dfs(neighbor, path)
                path.pop()  # Backtrack
        
        dfs(0, [0])
        return result


