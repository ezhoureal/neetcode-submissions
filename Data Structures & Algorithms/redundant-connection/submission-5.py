class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        union = [i for i in range(n + 1)]
        rank = [1] * (n + 1)
        def find(a):
            cur = a
            while union[cur] != cur:
                union[cur] = union[union[cur]]
                cur = union[cur]
            return cur
        def unite(a, b):
            head_a, head_b = find(a), find(b)
            if head_a == head_b:
                return False
            if rank[head_a] < rank[head_b]:
                union[head_a] = head_b
                rank[head_b] += rank[head_a]
            else:
                union[head_b] = head_a
                rank[head_a] += rank[head_b]
            return True
        
        for a, b in edges:
            if not unite(a, b):
                return [a,b]
        return []