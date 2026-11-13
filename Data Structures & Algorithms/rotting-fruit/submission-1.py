class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        m, n = len(grid), len(grid[0])
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0: return 0
        days = -1
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            days += 1
            for i in range(len(q), 0, -1):
                i,j = q.popleft()
                for nei in neighbors:
                    new_i, new_j = i + nei[0], j + nei[1]
                    if new_i < 0 or new_i >= m or new_j < 0 or new_j >= n:
                        continue
                    if grid[new_i][new_j] == 1:
                        grid[new_i][new_j] = 2
                        q.append((new_i, new_j))
                        fresh -= 1
        return days if fresh == 0 else -1