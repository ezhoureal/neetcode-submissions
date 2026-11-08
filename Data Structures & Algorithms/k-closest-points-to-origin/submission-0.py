import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(math.sqrt(p[0] ** 2 + p[1] ** 2), p) for p in points]
        heap = heapq.nsmallest(k, distances, key=lambda x: x[0])
        res = [x[1] for x in heap]
        return res

        