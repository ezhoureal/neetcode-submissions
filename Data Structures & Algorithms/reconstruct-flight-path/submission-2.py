class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for a,b in sorted(tickets)[::-1]:
            adj[a].append(b)
        res = []
        
        def dfs(cur):
            while adj[cur]:
                last = adj[cur].pop()
                dfs(last)
            res.append(cur)
        dfs('JFK')
        return res[::-1]