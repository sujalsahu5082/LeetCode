
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # pal[i][j] = True if s[i:j+1] is a palindrome
        pal = [[False] * n for _ in range(n)]

        # Build palindrome table
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j] and (
                    length <= 2 or pal[i + 1][j - 1]
                ):
                    pal[i][j] = True

        # dp[i] = maximum number of palindromes
        # using the first i characters
        dp = [0] * (n + 1)

        for j in range(1, n + 1):
            # Option 1: Skip the current character
            dp[j] = dp[j - 1]

            # Option 2: Choose a palindrome ending at j - 1
            for i in range(j):
                if j - i >= k and pal[i][j - 1]:
                    dp[j] = max(dp[j], dp[i] + 1)

        return dp[n]