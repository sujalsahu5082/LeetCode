class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        ans = ""

        for i in range(n):
            ones = 0

            for j in range(i, n):
                if s[j] == '1':
                    ones += 1

                # We have exactly k ones
                if ones == k:
                    curr = s[i:j + 1]

                    # Update if:
                    # 1. We don't have an answer yet
                    # 2. Current substring is shorter
                    # 3. Same length but lexicographically smaller
                    if (not ans or
                        len(curr) < len(ans) or
                        (len(curr) == len(ans) and curr < ans)):
                        ans = curr

                    # Adding more characters will only make it longer
                    break

                # More than k ones -> cannot be valid
                if ones > k:
                    break

        return ans