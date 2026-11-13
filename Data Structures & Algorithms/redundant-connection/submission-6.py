class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        degree = [0] * (n + 1)
        adj = [[] for i in range(n + 1)]
        for a,b in edges:
            degree[a] += 1
            degree[b] += 1
            adj[a].append(b)
            adj[b].append(a)
        q = deque()
        for i in range(1, n + 1):
            if degree[i] == 1:
                q.append(i)
        free = set()
        while q:
            node = q.popleft()
            free.add(node)
            for neighbor in adj[node]:
                degree[neighbor] -= 1
                if degree[neighbor] == 1:
                    q.append(neighbor)
        cycle = [i for i in range(n + 1) if i not in free]
        for a,b in reversed(edges):
            if a in cycle and b in cycle:
                return [a,b]
        return []
        
