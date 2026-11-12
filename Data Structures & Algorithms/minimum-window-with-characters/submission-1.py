class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = {}
        for c in t:
            freq[c] = freq.get(c, 0) + 1
        l = 0
        freq_b = {}
        have, need = 0, len(freq)
        best = None
        for r in range(len(s)):
            freq_b[s[r]] = freq_b.get(s[r], 0) + 1
            if s[r] in freq and freq_b[s[r]] == freq[s[r]]:
                have += 1
            while have == need:
                freq_b[s[l]] -= 1
                if s[l] in freq and freq_b[s[l]] == freq[s[l]] - 1:
                    have -= 1
                    if best is None or r - l + 1 < len(best):
                        best = s[l:r+1]
                l += 1
        return best if best else ""