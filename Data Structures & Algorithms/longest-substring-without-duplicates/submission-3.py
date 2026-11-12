class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = {}
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] in visited:
                l = max(l, visited[s[r]] + 1)
            res = max(res, r - l + 1)
            visited[s[r]] = r
        return res
