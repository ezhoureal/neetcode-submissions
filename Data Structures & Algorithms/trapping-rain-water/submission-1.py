class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        right = [0] * n
        right[n - 1] = height[n - 1]
        for j in range(n - 2, -1, -1):
            right[j] = max(right[j + 1], height[j])
        accum = 0
        left = height[0]
        for i in range(1, n - 1):
            left = max(left, height[i])
            accum += min(left, right[i]) - height[i]
        return accum