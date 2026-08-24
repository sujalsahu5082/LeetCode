class Solution:
    def stoneGameVIII(self, stones):
        n = len(stones)

        # Build prefix sums
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        # If Alice takes all stones
        best = prefix[n]

        # Consider taking first i stones, where i >= 2
        for i in range(n - 1, 1, -1):
            best = max(best, prefix[i] - best)

        return best