def convert(seq: List[int]):
    strings = []
    n = len(seq)
    for i in range(n):
        single = ""
        for j in range(n):
            if j == seq[i]:
                single += 'Q'
            else:
                single += '.'
        strings.append(single)
    return strings

class Solution:
    def backtrack(self, res, n, i, running: List[int]):
        if i == n:
            res.append(convert(running))
            return
        for j in range(n):
            if j in running:
                continue

            flag = True
            for o_x, o_y in enumerate(running):
                if o_x - o_y == i - j or o_x + o_y == i + j:
                    flag = False
                    break
            if not flag:
                continue

            running.append(j)
            self.backtrack(res, n, i + 1, running)
            running.pop()
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        self.backtrack(res, n, 0, [])
        return res