class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = [0] * n
        adj = [[] for i in range(n)]
        for edge in prerequisites:
            adj[edge[0]].append(edge[1])
            in_degree[edge[1]] += 1
        q = deque(i for i in range(n) if in_degree[i] == 0)
        order = []
        while q:
            v = q.popleft()
            order.append(v)
            for t in adj[v]:
                in_degree[t] -= 1
                if in_degree[t] == 0:
                    q.append(t)
        return list(reversed(order)) if len(order) == n else []
