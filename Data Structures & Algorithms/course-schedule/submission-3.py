class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for i in range(n)]
        WHITE, BLACK, GRAY = 0, 1, 2
        for edge in prerequisites:
            adj[edge[0]].append(edge[1])
        colors = [WHITE] * n
        for v in range(n):
            if colors[v] != WHITE: continue
            stack = [(v, iter(adj[v]))]
            colors[v] = GRAY
            while stack:
                u, it = stack[-1]
                s = next(it, None)
                if s is None:
                    colors[u] = BLACK
                    stack.pop()
                elif colors[s] == GRAY:
                    return False
                elif colors[s] == WHITE:
                    colors[s] = GRAY
                    stack.append((s, iter(adj[s])))
        return True