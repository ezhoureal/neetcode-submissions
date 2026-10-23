class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        def square_sum(i):
            res = 0
            while i > 0:
                res += (i % 10) ** 2
                i = i // 10
            return res
        while n not in visited:
            visited.add(n)
            n = square_sum(n)
        return n == 1
