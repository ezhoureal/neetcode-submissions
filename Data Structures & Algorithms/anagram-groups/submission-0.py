def toFreq(s: str):
    freq = [0] * 26
    for c in s:
        idx = ord(c) - ord('a')
        freq[idx] += 1
    return tuple(freq)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        res = []
        for s in strs:
            f = toFreq(s)
            if f in groups:
                res[groups[f]].append(s)
            else:
                groups[f] = len(res)
                res.append([s])
        return res