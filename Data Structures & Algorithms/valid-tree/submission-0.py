class Solution:
    def dfs(self, parent, i, adjs, visited) -> bool:
        visited.add(i)
        for adj in adjs[i]:
            if adj == parent:
                continue
            if adj in visited:
                return False
            if not self.dfs(i, adj, adjs, visited):
                return False
        return True
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for i in range(n)]
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visited = set()
        if not self.dfs(-1, 0, adj, visited):
            return False
        return len(visited) == n
