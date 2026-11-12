class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = {}
        for c in s1:
            freq[c] = freq.get(c, 0) - 1
        l = 0
        for r in range(len(s2)):
            freq[s2[r]] = freq.get(s2[r], 0) + 1
            while freq[s2[r]] > 0:
                freq[s2[l]] -= 1
                l += 1
            if all(x == 0 for x in freq.values()):
                return True
        return False
            