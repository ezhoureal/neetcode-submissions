class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        freq = {}

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            while r - l + 1 > k + max(freq.values()):
                freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res