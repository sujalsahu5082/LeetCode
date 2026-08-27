class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Frequency of characters in s
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        ans = []

        # Match target as long as possible
        for i in range(n):
            x = ord(target[i]) - ord('a')

            if cnt[x] > 0:
                cnt[x] -= 1
                ans.append(target[i])
            else:
                # Cannot match target[i].
                # Try the smallest character greater than target[i].
                for c in range(x + 1, 26):
                    if cnt[c] > 0:
                        cnt[c] -= 1

                        res = ans + [chr(c + ord('a'))]

                        # Put remaining characters in sorted order
                        for j in range(26):
                            res.append(chr(j + ord('a')) * cnt[j])

                        return ''.join(res)

                # No greater character here.
                # We must change an earlier position.
                break

        # We matched all of target.
        # Or we got stuck.
        #
        # Go backwards through the matched prefix and try
        # replacing one character with a larger character.

        for i in range(len(ans) - 1, -1, -1):

            # Return ans[i] to the available characters
            c = ord(ans[i]) - ord('a')
            cnt[c] += 1

            # Find the smallest character greater than ans[i]
            for bigger in range(c + 1, 26):
                if cnt[bigger] > 0:
                    cnt[bigger] -= 1

                    res = ans[:i] + [chr(bigger + ord('a'))]

                    # Remaining characters in sorted order
                    for j in range(26):
                        res.append(chr(j + ord('a')) * cnt[j])

                    return ''.join(res)

        return ""