class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # count the Out-degree if O-d == 0, judge dont trust
        # In-degree == N - 1, everyone trusts him
        if  n == 1 and not trust:
            return 1
        # In-degree
        in_degree = [0] * (n + 1) 
        
        # Out-degree
        out_degree = [0] * (n + 1)

        # traverse through edges
        # a trust b
        for a ,b in trust:
            out_degree[a] += 1
            in_degree[b] += 1
        
        for i in range(1, n + 1):
            # Condition: getting N-1 people trust and no one trusts
            if in_degree[i] == n - 1 and out_degree[i] == 0:
                return i
                
        return -1
