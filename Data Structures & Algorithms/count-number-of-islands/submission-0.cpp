class Solution {
public:
    void bfs(vector<vector<char>>& grid, int x, int y) {
        constexpr std::array<int, 4> dx = {0, 0, -1, 1};
        constexpr std::array<int, 4> dy = {-1, 1, 0, 0};
        queue<pair<int, int>> q;
        q.push({x, y});
        while (!q.empty()) {
            const auto [x, y] = q.front();
            q.pop();
            for (int i = 0; i < 4; ++i) {
                int new_x = x + dx[i];
                int new_y = y + dy[i];
                if (new_x < 0 || new_x >= grid[0].size()) continue;
                if (new_y < 0 || new_y >= grid.size()) continue;
                if (grid[new_y][new_x] == '1') {
                    grid[new_y][new_x] = 0;
                    q.push({new_x, new_y});
                }
            }
        }
    }
    int numIslands(vector<vector<char>>& grid) {
        int count = 0;
        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[0].size(); ++j) {
                if (grid[i][j] == '1') {
                    bfs(grid, j, i);
                    ++count;
                }
            }
        }
        return count;
    }
};
