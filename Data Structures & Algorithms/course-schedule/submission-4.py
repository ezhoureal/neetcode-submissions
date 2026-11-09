class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        in_deg = [0] * n
        adj = [[] for _ in range(n)]
        for edge in prerequisites:
            in_deg[edge[1]] += 1
            adj[edge[0]].append(edge[1])
        q = deque(i for i in range(n) if in_deg[i] == 0)
        order = []
        while q:
            i = q.popleft()
            order.append(i)
            for child in adj[i]:
                in_deg[child] -= 1
                if in_deg[child] == 0:
                    q.append(child)
        return len(order) == n
        